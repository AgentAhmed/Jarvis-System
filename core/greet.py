import datetime
import re
from .speech import speak

def wish_user(name=None):
    hour = datetime.datetime.now().hour
    greet = "Good morning" if hour < 12 else "Good afternoon" if hour < 18 else "Good evening"
    if name:
        speak(f"{greet} {name}! I am Jarvis. How can I assist you today?")
    else:
        speak(f"{greet} sir! I am Jarvis. Please tell me how I can assist you.")

def extract_name(query):
    match = re.search(r"(my name is|i am)\s+([a-zA-Z]+)", query)
    if match:
        return match.group(2).capitalize()
    return None
