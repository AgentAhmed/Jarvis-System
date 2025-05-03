import webbrowser
import os
from .speech import speak

def handle_command(query):
    if "open notepad" in query:
        os.system("notepad")
        speak("Opening Notepad.")
    elif "open google" in query:
        webbrowser.open("https://www.google.com")
        speak("Opening Google.")
    elif "play music" in query:
        music_path = "F:\Songs\Black Rebel Motorcycle Club - Beat the Devil's Tattoo.mp3"  # Replace with your local file
        os.startfile(music_path)
        speak("Playing music.")
    else:
        speak("Sorry, I don't recognize that command.")
