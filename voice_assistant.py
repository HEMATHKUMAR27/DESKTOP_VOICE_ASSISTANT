import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import webbrowser
listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)
def talk(text):
    engine.say(text)
    engine.runAndWait( )
def take_command():
    command = None
    try:
        with sr.Microphone() as source:
            print("Listening...")
            talk("Listening...")
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
    except Exception as e:
        print(f"An error occurred: {e}")
    return command
def run_alexa():
    command = take_command()
    if 'quit' in command:
        return "quit"
    if 'alexa' in command:
        command = command.replace('alexa','').strip()
    order= command
    print(command)
    if 'play' in command:
        song = command.replace('play','')
        talk('Playing'+ song)
        pywhatkit.playonyt(song)
    elif 'time' in command:
        time = datetime.datetime.now().strftime("%I:%M %p")
        talk('Current time'+time)
    elif 'who is' in command:
        person = command.replace('who is','').strip()
        info = wikipedia.summary(person,10)
        print(info)
        talk(info)
    elif 'open google' in command:
        talk("Opening Google")
        webbrowser.open("https://www.google.com")
    elif 'search' in command:
        query = command.replace("search",'')
        webbrowser.open(f"https://www.google.com/search?q={query}")
    return order
a=run_alexa()
while a!="quit":
    a=run_alexa()