import speech_recognition as sr 
import pyttsx3
import logging
import os 

# This is Logger for the application
LOG_DIR = "logs"
LOG_FILE_NAME = "application.log"

os.makedirs(LOG_DIR,exist_ok = True)

log_path = os.path.join(LOG_DIR,LOG_FILE_NAME)

logging.basicConfig(
    filename=log_path,
    format="[%(asctime)s] %(name)s - %(levelname)s - %(message)s",
    level= logging.INFO,
)


# Taking the male voice from my system

engine = pyttsx3.init('sapi5') # sapi5 is a parameter of voice system

voices = engine.getProperty('voices')
print(voices)

# for i in voices:
#     print(i.id)

engine.setProperty('voice',voices[0].id)

def speak(text):
    engine.say(text)
    engine.runAndWait()
    
# speak("Hello , I am Jarvis. How can I assist you.") 

def takeCommand():
    r = sr.Recognizer()   
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source) 
        
    try:
        print('Recognizing...')
        query = r.recognize_google(audio, language="en-in")
        print(f"User said : {query}\n")
    except Exception as e:
        logging.info(e)
        print("Say that again please")
        return "None"
    return query

text = takeCommand()
speak(text)           
        
        