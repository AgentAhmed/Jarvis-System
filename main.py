import speech_recognition as sr 
import pyttsx3

# Taking the male voice from my system

engine = pyttsx3.init('sapi5') # sapi5 is a parameter of voice system

voices = engine.getProperty('voices')
print(voices)

# for i in voices:
#     print(i.id)

engine.setProperty('voice',voices[0].id)

engine.say("Hello , How can I assist you ?")
engine.runAndWait()
