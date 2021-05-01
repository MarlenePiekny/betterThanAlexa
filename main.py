# This is my kind of Alexa Project, my first project in Python

#Import Python packages
#Vocal recognition
import speech_recognition as sr
#Text to speech
import pyttsx3

listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[3].id)

engine.say("Bonjour! Que puis-je faire pour vous?")
print("Bonjour! Que puis-je faire pour vous?")
engine.runAndWait()

try:
    with sr.Microphone() as source:
        engine.say("Je vous écoute...")
        print("Je vous écoute...")
        engine.runAndWait()
        voice = listener.listen(source)
        command = listener.recognize_google(voice)
        command = command.lower()
        if 'alexa' in command:
            engine.say(command)
            print(command)

except:
    pass
