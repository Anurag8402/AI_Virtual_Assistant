import speech_recognition as sr
import speak  # Make sure this module exists and has a 'speak' function

def speech_to_text():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        audio = r.listen(source)
        try:
            voice_data = r.recognize_google(audio)
            return voice_data
        except sr.UnknownValueError:
            speak.speak("Sorry, I did not understand that.")
        except sr.RequestError:
            speak.speak("No internet connection. Please turn on your internet.")

# This block should be OUTSIDE the function
if __name__ == "__main__":
    text = speech_to_text()
    if text:
        print("You said:", text)
