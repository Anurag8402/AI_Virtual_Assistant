import pyttsx3

engine = pyttsx3.init()
engine.setProperty('rate', 150)  # Adjust speed (default is ~200)

def speak(text):
    engine.say(text)
    engine.runAndWait()
