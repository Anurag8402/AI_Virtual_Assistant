🤖 AI Virtual Assistant – Python Desktop App
================================================

A Python-based voice-enabled virtual assistant that understands your commands and performs smart tasks like note-taking, web browsing, AI conversation, and app/file automation.

-------------------------------------------------
🚀 Features
-------------------------------------------------
- 🎙️ Voice command recognition using speech recognition
- 🧠 ChatGPT-powered responses via OpenAI API
- 📝 Create, read, and delete notes with voice commands
- 🌐 Web search and YouTube playback
- 📂 Open files, folders, or desktop applications
- 🖥️ Expandable for smart routines, calendar, and email features

-------------------------------------------------
🛠️ Technologies Used
-------------------------------------------------
- Python 3.x
- speech_recognition – Voice input
- pyttsx3 – Text-to-speech output
- openai – ChatGPT integration
- pywhatkit – YouTube search, Google search
- os, webbrowser, datetime – Core task utilities
- tkinter or PyQt – (Optional GUI)

-------------------------------------------------
🧠 Assistant Capabilities
-------------------------------------------------
| Function           | Example Command                      |
|--------------------|--------------------------------------|
| Chat with AI       | “Hey assistant, tell me a joke”      |
| Take a note        | “Remember this: buy groceries”       |
| Read notes         | “Show me my notes”                   |
| Web search         | “Search Python tutorial on Google”   |
| Play video         | “Play lo-fi music on YouTube”        |
| Open apps/folders  | “Open Downloads folder”              |
| Time & date        | “What’s the time?” / “Today’s date?” |

-------------------------------------------------
📁 Project Structure
-------------------------------------------------
AI_Virtual_Assistant/
├── assistant/
│   ├── recognizer.py          
│   ├── speaker.py             
│   ├── command_processor.py  
│   ├── openai_chat.py        
│   ├── note_manager.py        
│   └── main.py               
├── assets/
│   └── beep.wav              
├── requirements.txt           
└── README.md                

-------------------------------------------------
🔧 Setup Instructions
-------------------------------------------------
1. Clone the Repository
   git clone https://github.com/yourusername/ai-virtual-assistant.git
   cd ai-virtual-assistant

2. Create a Virtual Environment (Optional)
   python -m venv venv
   venv\Scripts\activate  # On Windows

3. Install Dependencies
   pip install -r requirements.txt

4. Set OpenAI API Key (for ChatGPT Integration)
   # Linux/macOS
   export OPENAI_API_KEY="your-api-key"

   # Windows
   set OPENAI_API_KEY="your-api-key"

5. Run the Assistant
   python assistant/main.py

-------------------------------------------------
🔐 Optional Features to Add
-------------------------------------------------
- Email and calendar access (IMAP, Google API)
- Wake word detection (e.g., “Hey Jarvis”)
- Smart routines & reminders
- Multilingual voice support
- GUI interface using Tkinter or PyQt

-------------------------------------------------
📸 Demo
-------------------------------------------------
Voice Assistant GUI Interface  
![A1](https://github.com/user-attachments/assets/4d0b732b-fbb0-4748-bdf8-8a9d803812b5)


Command Line: Playing YouTube Video  
![A2](https://github.com/user-attachments/assets/fc755ec4-6e0a-4e2a-90ee-f80c1b8192f4)


-------------------------------------------------
👨‍💻 Author
-------------------------------------------------
Anurag Yadav  
GitHub: https://github.com/Anurag8402

-------------------------------------------------
📄 License
-------------------------------------------------
This project is licensed under the MIT License.
    
