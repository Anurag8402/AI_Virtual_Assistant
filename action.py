import datetime
import time
import re
import sys
import pyttsx3
import speech_recognition as sr
import speak
import webbrowser
import chatgpt_ai
import random
import weather
import os
import wikipedia
import wolframalpha
from datetime import datetime

# Initialize WolframAlpha client
wolfram_client = wolframalpha.Client("Replace with your WolframAlpha App ID")  # Replace with your WolframAlpha App ID
engine = pyttsx3.init()


def listen_for_input():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        try:
            audio = recognizer.listen(source, timeout=6)
            text = recognizer.recognize_google(audio, language='en-IN')
            return text.lower()
        except:
            return None


def do_breathing_exercise():
    speak("Let's do a short breathing exercise. Inhale slowly...")
    time.sleep(4)
    speak("Hold it...")
    time.sleep(4)
    speak("Now exhale gently...")
    time.sleep(4)
    speak("Great job. You’re already doing better.")

def give_mindfulness_tip():
        tips = [
            "Close your eyes for 30 seconds and just focus on your breath.",
            "Gratitude reduces stress. Think of 3 things you're thankful for.",
            "Take a walk, even a short one. Movement resets your mind.",
            "Drink a glass of water slowly and mindfully.",
            "Silence your devices and just be present for 2 minutes."
        ]
        tip = random.choice(tips)
        speak(tip)

def speak(text):
    engine.say(text)
    engine.runAndWait()

def take_note():
    speak("What should I write?")
    recognizer = sr.Recognizer()
    recognizer.pause_threshold = 1.3
    recognizer.energy_threshold = 300
    recognizer.dynamic_energy_threshold = True

    with sr.Microphone() as source:
        print("Adjusting for background noise...")
        recognizer.adjust_for_ambient_noise(source, duration=1)
        print("Listening for your note...")
        try:
            audio = recognizer.listen(source, timeout=8)
        except sr.WaitTimeoutError:
            print("Listening timed out.")
            speak("Timed out. Please try again.")
            return "Timed out."

    try:
        print("Recognizing...")
        note = recognizer.recognize_google(audio, language='en-IN')

        if note.strip():
            note = note.strip().capitalize()
            timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            with open("notes.txt", "a", encoding='utf-8') as f:
                f.write(f"[{timestamp}] {note}\n")
            print("Saved:", note)
            speak("Note saved.")
            return "Note saved."
        else:
            speak("Didn't catch that.")
            return "Empty note."

    except sr.UnknownValueError:
        print("Didn't understand.")
        speak("Sorry, I couldn't understand.")
        return "Unclear."
    except sr.RequestError as e:
        print(f"API error: {e}")
        speak("Speech service issue.")
        return "API error."

def Action(send):
  
    data_btn  = send.lower()

    if "what is your name" in   data_btn :
      speak("my name is virtual Assistant")
      return "my name is virtual Assistant"

    elif "hello" in data_btn  or "hye" in data_btn  or "hay" in data_btn or "hi" in data_btn:
        speak("Hey sir, How i can  help you !")
        return "Hey sir, How i can  help you !" 

    elif "how are you" in  data_btn :
            speak("I am doing great these days sir")
            return "I am doing great these days sir"   

    elif "thanku" in data_btn or "thank" in data_btn:
           speak("its my pleasure sir to stay with you")
           return "its my pleasure sir to stay with you"      

    elif "good morning" in data_btn:
           speak("Good morning sir, i think you might need some help")
           return "Good morning sir, i think you might need some help"


    elif 'search' in data_btn:

        search_query = data_btn.replace("search", "").strip()

        if search_query:

            try:

                # First, search on Google

                webbrowser.open(f"https://www.google.com/search?q={search_query}")

                speak(f"Searching Google for {search_query}")

                res = wolfram_client.query(search_query)

                answer = next(res.results).text

                speak(answer)

                return f"WolframAlpha result: {answer}"


            except Exception:

                summary = wikipedia.summary(search_query, sentences=2)

                speak(summary)

                return f"Wikipedia Summary: {summary}"

    elif data_btn.startswith("chat:") or "talk to ai" in data_btn:
            query = data_btn.replace("chat:", "").strip()
            if query:
                response = chatgpt_ai.chat_with_ai(query)
                speak(response)
                return response
            else:
                speak("Please ask me something.")
                return "Please ask me something."


    elif "close application" in data_btn or "close app" in data_btn or "stop program" in data_btn:

        speak("Sure. Please type the name of the application you want to close.")

        app_name = input("Enter the application name to close: ")  # TEXT INPUT

        if app_name:

            # Mapping of user-friendly names to actual process names

            app_map = {

                "notepad": "notepad.exe",

                "chrome": "chrome.exe",

                "browser": "chrome.exe",

                "spotify": "Spotify.exe",

                "vs code": "Code.exe",

                "word": "WINWORD.EXE",

                "excel": "EXCEL.EXE",

                "powerpoint": "POWERPNT.EXE",

                "cmd": "cmd.exe",

                "terminal": "cmd.exe"

            }

            process_name = app_map.get(app_name.lower().strip())

            if process_name:

                os.system(f"taskkill /f /im {process_name}")

                speak(f"{app_name.capitalize()} closed successfully.")

                return f"{app_name.capitalize()} closed successfully."

            else:

                speak(f"Sorry, I don't recognize {app_name}. Please try with a known app.")

                return "Unknown app name."

        else:

            speak("No application name was entered. Please try again.")

            return "No app name received."

    elif 'who is' in data_btn or 'what is' in data_btn:

          speak("Searching Wikipedia...")
          data_btn = data_btn.replace("who is", "").replace("what is", "")
          result = wikipedia.summary(data_btn, sentences=2)
          speak(result)
          return result



    elif "time now" in data_btn or "time" in data_btn:
          current_time = datetime.datetime.now()
          Time = (str)(current_time.hour)+ " Hour : ", (str)(current_time.minute) + " Minute" 
          speak(Time)
          return str(Time) 

    elif "shutdown" in data_btn or "quit" in data_btn:
            speak("ok sir")
            return "ok sir"  

    elif "play music" in data_btn or "song" in data_btn:
        webbrowser.open("https://open.spotify.com/")
        speak("spotify.com is now ready for you, enjoy your music")
        return "spotify.com is now ready for you, enjoy your music"


    elif 'open google' in data_btn or 'google'  in data_btn:
        url = 'https://google.com/'
        webbrowser.get().open(url)
        speak("google open")
        return "google open"

    elif 'youtube' in data_btn or "open youtube" in  data_btn:
        url = 'https://youtube.com/'
        webbrowser.get().open(url)
        speak("YouTube open")
        return "YouTube open"

    elif 'whatsapp' in data_btn :
        url  = 'https://web.whatsapp.com/'
        webbrowser.get().open(url)
        speak("Whatapp open")
        return "Whatapp open"

    elif 'chatgpt' in data_btn :
        url  = 'https://chatgpt.com/'
        webbrowser.get().open(url)
        speak("chatgpt open")
        return "chatgpt open"

    elif 'instagram' in data_btn :
        url  = 'https://www.instagram.com /'
        webbrowser.get().open(url)
        speak("Instagram open")
        return "Instagram open"

    elif 'github' in data_btn :
        url  = 'https://github.com /'
        webbrowser.get().open(url)
        speak("github open")
        return "github open"

    elif "close assistant" in data_btn or "exit assistant" in data_btn or "turn off assistant" in data_btn:
        speak("Closing the virtual assistant. Goodbye!")
        sys.exit()

    elif 'map' in data_btn or 'google map' in data_btn:
        url = 'https://www.google.com/maps'
        webbrowser.open(url)
        speak("Google Maps opened")
        return "Google Maps opened"

    elif 'amazon' in data_btn:
        url = 'https://www.amazon.in'
        webbrowser.open(url)
        speak("Amazon opened")
        return "Amazon opened"

    elif 'netflix' in data_btn:
        url = 'https://www.netflix.com'
        webbrowser.open(url)
        speak("Netflix opened")
        return "Netflix opened"

    elif "open notepad" in data_btn or "launch notepad" in data_btn:
        speak("Opening Notepad")
        os.system("notepad.exe")
        return "Notepad opened"

    elif 'facebook' in data_btn:
        url = 'https://www.facebook.com'
        webbrowser.open(url)
        speak("Facebook opened")
        return "Facebook opened"

    elif 'instagram' in data_btn:
        url = 'https://www.instagram.com'
        webbrowser.open(url)
        speak("Instagram opened")
        return "Instagram opened"

    elif 'hotstar' in data_btn or 'disney plus' in data_btn:
        url = 'https://www.hotstar.com/in'
        webbrowser.open(url)
        speak("Hotstar opened")
        return "Hotstar opened"

    elif 'prime video' in data_btn or 'amazon prime' in data_btn:
        url = 'https://www.primevideo.com'
        webbrowser.open(url)
        speak("Amazon Prime Video opened")
        return "Amazon Prime Video opened"

    elif 'flipkart' in data_btn:
        url = 'https://www.flipkart.com'
        webbrowser.open(url)
        speak("Flipkart opened")
        return "Flipkart opened"

    elif 'gmail' in data_btn:
        url = 'https://mail.google.com'
        webbrowser.open(url)
        speak("Gmail opened")
        return "Gmail opened"

    elif 'google photos' in data_btn or 'photos' in data_btn:
        url = 'https://www.google.com/photos/about/'
        webbrowser.open(url)
        speak("Google Photos opened")
        return "Google Photos opened"

    elif 'google docs' in data_btn or 'documents' in data_btn:
        url = 'https://docs.google.com/document/d/1sWsv0bB0ootbwUSe9HjM6a4RAVCxrpsKmHjqMGb3jA8/edit?addon_store&tab=t.0'
        webbrowser.open(url)
        speak("Google Docs opened")
        return "Google Docs opened"



    elif "take a note" in data_btn or "write a note" in data_btn or "make a note" in data_btn or "save note" in data_btn:

        result = take_note()

        return result

    elif any(keyword in data_btn for keyword in ["calculate", "what is", "what's", "solve"]):
        # Extract the math expression from the command
        expr = data_btn

        # Remove keywords that trigger calculation
        expr = expr.replace("calculate", "").replace("what is", "").replace("what's", "").replace("solve", "").strip()

        # Replace common words with math operators
        expr = expr.replace("plus", "+")
        expr = expr.replace("minus", "-")
        expr = expr.replace("times", "*")
        expr = expr.replace("multiplied by", "*")
        expr = expr.replace("x", "*")
        expr = expr.replace("divided by", "/")
        expr = expr.replace("over", "/")

        # Remove any unwanted characters, just keep numbers, operators, dots and spaces
        expr = re.sub(r"[^0-9\+\-\*\/\. ]", "", expr)

        try:
            # Evaluate the expression safely
            answer = eval(expr)
            response = f"The answer is {answer}"
            speak(response)
            return response
        except Exception as e:
            speak("Sorry, I couldn't calculate that.")
            return "Calculation error."

    elif "i'm feeling stressed" in data_btn or "i need to relax" in data_btn or "help me calm down" in data_btn:

            speak("I'm here for you. Let's take a deep breath together.")
            time.sleep(1)
            speak("Inhale... and exhale.")
            time.sleep(2)
            speak("Would you like:")
            speak("Option 1. Calm music")
            speak("Option 2. A breathing exercise")
            speak("Option 3. Mindfulness tips")
            speak("Please say music, breathing, or tips.")

            choice = listen_for_input()  # This must be a function that listens and returns recognized speech as text

    if choice:
            choice = choice.lower()

            if "music" in choice:
                webbrowser.open("https://www.youtube.com/watch?v=2OEL4P1Rz04")
                speak("Playing relaxing music now.")
                return "Relaxing music playing."


            elif "breathing" in choice or "exercise" in choice:
                do_breathing_exercise()
                return "Breathing exercise done."


            elif "tips" in choice or "mindfulness" in choice:
                give_mindfulness_tip()
                return "Mindfulness tip shared."


            else:
                    speak("I didn't get that. You can say music, breathing, or tips.")

                    return "User response unclear."

    else :
        speak( "i'm unable to understand!")
        return "i'm unable to understand!"

