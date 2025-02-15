import datetime
import speak
import webbrowser
import weather
import os


def Action(send) :   
  
    data_btn  = send.lower()

    if "what is your name" in   data_btn :
      speak.speak("my name is virtual Assistant")  
      return "my name is virtual Assistant"

    elif "hello" in data_btn  or "hye" in data_btn  or "hay" in data_btn or "hi" in data_btn:
        speak.speak("Hey sir, How i can  help you !")  
        return "Hey sir, How i can  help you !" 

    elif "how are you" in  data_btn :
            speak.speak("I am doing great these days sir") 
            return "I am doing great these days sir"   

    elif "thanku" in data_btn or "thank" in data_btn:
           speak.speak("its my pleasure sir to stay with you")
           return "its my pleasure sir to stay with you"      

    elif "good morning" in data_btn:
           speak.speak("Good morning sir, i think you might need some help")
           return "Good morning sir, i think you might need some help"   

    elif "time now" in data_btn or "time" in data_btn:
          current_time = datetime.datetime.now()
          Time = (str)(current_time.hour)+ " Hour : ", (str)(current_time.minute) + " Minute" 
          speak.speak(Time)
          return str(Time) 

    elif "shutdown" in data_btn or "quit" in data_btn:
            speak.speak("ok sir")
            return "ok sir"  

    elif "play music" in data_btn or "song" in data_btn:
        webbrowser.open("https://open.spotify.com/")
        speak.speak("spotify.com is now ready for you, enjoy your music")
        return "spotify.com is now ready for you, enjoy your music"


    elif 'open google' in data_btn or 'google'  in data_btn:
        url = 'https://google.com/'
        webbrowser.get().open(url)
        speak.speak("google open")  
        return "google open"

    elif 'youtube' in data_btn or "open youtube" in  data_btn:
        url = 'https://youtube.com/'
        webbrowser.get().open(url)
        speak.speak("YouTube open") 
        return "YouTube open"    
    
    elif 'weather' in data_btn :
       ans   = weather.Weather()
       speak.speak(ans) 
       return ans

    elif 'whatapp' in data_btn :
        url  = 'https://web.whatsapp.com/'
        webbrowser.get().open(url)
        speak.speak("Whatapp open")
        return "Whatapp open"

    elif 'chatgpt' in data_btn :
        url  = 'https://chatgpt.com/'
        webbrowser.get().open(url)
        speak.speak("chatgpt open")
        return "chatgpt open"

    elif 'instagram' in data_btn :
        url  = 'https://www.instagram.com /'
        webbrowser.get().open(url)
        speak.speak("Instagram open")
        return "Instagram open"

    elif 'github' in data_btn :
        url  = 'https://github.com /'
        webbrowser.get().open(url)
        speak.speak("github open")
        return "github open"

    else :
        speak.speak( "i'm unable to understand!")
        return "i'm unable to understand!"

