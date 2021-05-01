# This is my kind of Alexa Project, my first project in Python

#Import Python packages
#Vocal recognition
import speech_recognition as sr
#Text to speech
import pyttsx3
#
import pywhatkit

listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

def talk(text):
    engine.say(text)
    print(text)
    engine.runAndWait()

talk('Bonjour, je suis Lilou Dallas! Que puis-je faire pour vous?')

def take_command():
    try:
        with sr.Microphone() as source:
            talk('Je vous écoute...')
            voice = listener.listen(source)
            command = listener.recognize_google(voice, language="fr-FR")
            command = command.lower()
            print(command)
    except:
        pass
    return command

def run_alexa():
    command = take_command()

    if 'joue' in command:
        song = command.replace('joue', '')
        talk('Je joue' + song)
        pywhatkit.playonyt(song)

run_alexa()