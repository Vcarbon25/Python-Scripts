"""
dependencies
pip install pyttsx3
pip install speech_recognition
https://pypi.org/project/SpeechRecognition/
pip install PyAudio
"""
import pyttsx3
import speech_recognition as sr
def Speak(Text):
    engine = pyttsx3.init()
    engine.say(Text)
    engine.runAndWait()

Speak("First Sound emgine test")

r= sr.Recognizer()
with sr.Microphone() as source:
    #hear part
    print("Fale: ")
    audio=r.listen(source)
    #understanding part
    try:
        Spoken = r.recognize_google(audio)
    except:
        Spoken = sr.RequestError()

print("was said: "+Spoken)