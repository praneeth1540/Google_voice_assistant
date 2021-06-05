import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes
import temp

from googlesearch import search
listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)


def talk(text):
    engine.say(text)
    engine.runAndWait()

talk(" hi ! How can i help you")
def take_command():
    try:
        global commandd
        with sr.Microphone() as source:
            print('listening....')
            voice = listener.listen(source)
            commandd = listener.recognize_google(voice)
            commandd = commandd.lower()
            if 'alexa' in commandd:
                commandd=commandd.replace('alexa','')
                print(commandd)

    except:
        pass
    return commandd

def run_alexa():
    command = take_command()
    print(command)
    if 'play' in command:
        song=command.replace('play','')
        talk("playing"+song)
        pywhatkit.playonyt(song)
    elif 'time' in command:
        time=datetime.datetime.now().strftime('%I;%M %p')
        talk('Current time in india is' + time)
    elif 'who is'  in command :
        person = command.replace('who is',"")
        info=wikipedia.summary(person,1)
        talk(info)
    elif 'what is'  in command :
        person = command.replace('who is',"")
        info=wikipedia.summary(person,1)
        talk(info)
    elif "joke" in command:
        talk(pyjokes.get_joke())
    elif "how are you" in command:
        talk("i am fine,  thank you for asking . i hope you and your loved ones are staying safe and healthy")
    elif "temperature" in command:




while True:
    run_alexa()