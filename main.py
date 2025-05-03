import os
import logging
from core.speech import speak, take_command
from core.greet import wish_user, extract_name
from core.commands import handle_command

# Setup logging
os.makedirs("logs", exist_ok=True)
logging.basicConfig(
    filename="logs/application.log",
    format="[%(asctime)s] %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO,
)

# Main logic
user_name = None
wish_user()

while True:
    query = take_command()

    if any(kw in query for kw in ["exit", "shutdown", "bye", "stop"]):
        speak("Goodbye! Have a great day.")
        break

    # Store user name
    name = extract_name(query)
    if name:
        user_name = name
        speak(f"Nice to meet you, {user_name}!")

    # Small talk
    elif "how are you" in query and user_name:
        speak(f"I'm great, {user_name}. What can I help you with?")
    elif "how are you" in query:
        speak("I'm good, sir. May I know your name?")

    # Functional tasks
    else:
        handle_command(query)
