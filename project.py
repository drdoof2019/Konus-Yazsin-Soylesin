# https://www.mertmekatronik.com/turkce-speech-recognition
# https://tr.linkedin.com/pulse/pythonda-sesli-asistan-olu%C5%9Fturmak-yunus-emre-g%C3%BCndo%C4%9Fmu%C5%9F
# Çıkan sorunu şu linkl çözdüm
# https://stackoverflow.com/questions/55984129/attributeerror-could-not-find-pyaudio-check-installation-cant-use-speech-re
import speech_recognition as sr

#metni sese dönüştürmek için
from gtts import gTTS
#sistem dosyalarını daha rahat şekilde açmak için
import os

r = sr.Recognizer()

with sr.Microphone() as source:
    r.adjust_for_ambient_noise(source)
    print("Arka plan gürültüsü:" + str(r.energy_threshold))

    try:
        ses = r.listen(source, timeout=2, phrase_time_limit=7)
        yazi = r.recognize_google(ses, language='tr-tr')
        print(yazi)
        tts = gTTS(yazi, lang='tr')
        tts.save("output.mp3")
        os.system("output.mp3")
    except sr.WaitTimeoutError:
        print("Dinleme zaman aşımına uğradı")

    except sr.UnknownValueError:
        print("Ne dediğini anlayamadım")

    except sr.RequestError:
        print("İnternete bağlanamıyorum")
