import speech_recognition as sr
import pyttsx3
import logging
import os
import datetime
import re

# Setup logging
LOG_DIR = "logs"
LOG_FILE_NAME = "application.log"
os.makedirs(LOG_DIR, exist_ok=True)
log_path = os.path.join(LOG_DIR, LOG_FILE_NAME)
logging.basicConfig(
    filename=log_path,
    format="[%(asctime)s] %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO,
)

# Initialize TTS engine
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

def speak(text):
    engine.say(text)
    engine.runAndWait()

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print('Recognizing...')
        query = r.recognize_google(audio, language="en-in")
        print(f"User said: {query}\n")
    except Exception as e:
        logging.info(e)
        print("Say that again please...")
        return "None"
    return query.lower()

def wish_me(name=None):
    hour = datetime.datetime.now().hour
    if hour < 12:
        greet = "Good morning"
    elif hour < 18:
        greet = "Good afternoon"
    else:
        greet = "Good evening"

    if name:
        speak(f"{greet} {name}! I am Jarvis. How can I assist you today?")
    else:
        speak(f"{greet} sir! I am Jarvis. Please tell me how can I assist you?")

def extract_name(text):
    match = re.search(r"(my name is|i am)\s+([a-zA-Z]+)", text)
    if match:
        return match.group(2).capitalize()
    return None

# 🧠 Main program loop
user_name = None
wish_me()

while True:
    query = takeCommand().lower()

    # Exit command
    if any(kw in query for kw in ["exit", "bye", "shutdown", "stop"]):
        speak("Goodbye sir! Have a great day.")
        break

    # Detect and store name
    name = extract_name(query)
    if name:
        user_name = name
        speak(f"Nice to meet you, {user_name}!")

    # Personalized greeting if name is known
    if "how are you" in query and user_name:
        speak(f"I am always good when I talk to you, {user_name}. What can I do for you?")
    elif "how are you" in query:
        speak("I am good, sir. What's your name?")

    # Echo back what the user says
    else:
        speak(f"You said: {query}")
