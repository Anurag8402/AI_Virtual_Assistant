🤖 AI Virtual Assistant – Python Project
A Python-based voice-enabled virtual assistant capable of understanding user commands and performing smart tasks like note-taking, web search, AI chat, and more.

🚀 Features
🎙️ Voice command recognition

🧠 ChatGPT-powered responses (OpenAI API)

📝 Smart note-taking (create, read, delete notes)

🌐 Web search and browser interaction

📂 File and folder automation (open apps, folders)

🛠️ Technologies Used
Python 3.x

speech_recognition – Voice input

pyttsx3 – Text-to-speech

openai – ChatGPT integration

pywhatkit – YouTube search, web search

datetime, os, webbrowser – Core tasks

tkinter or PyQt – (Optional GUI)

🧠 Assistant Capabilities
Function	Example Command
Chat with AI	"Hey assistant, tell me a joke"
Take a note	"Remember this: buy groceries"
Read notes	"Show me my notes"
Web search	"Search Python tutorial on Google"
Play video	"Play lo-fi music on YouTube"
Open apps/folders	"Open Downloads folder"
Time & date	"What’s the time?" / "Today’s date?"

📁 Project Structure
bash
Copy
Edit
AI_Virtual_Assistant/
├── assistant/
│   ├── recognizer.py         # Voice recognition logic
│   ├── speaker.py            # Text-to-speech handler
│   ├── command_processor.py  # Task & intent handler
│   ├── openai_chat.py        # ChatGPT/OpenAI interaction
│   ├── note_manager.py       # Notes creation and reading
│   └── main.py               # Entry point
├── assets/
│   └── beep.wav              # Optional sounds
├── requirements.txt
└── README.md
🔧 Setup Instructions
Clone the repository

bash
Copy
Edit
git clone https://github.com/yourusername/ai-virtual-assistant.git
cd ai-virtual-assistant
Create virtual environment (optional)

bash
Copy
Edit
python -m venv venv
venv\Scripts\activate  # Windows
Install dependencies

bash
Copy
Edit
pip install -r requirements.txt
Set OpenAI API key (if using GPT)

bash
Copy
Edit
export OPENAI_API_KEY="your-api-key"  # Linux/macOS
set OPENAI_API_KEY="your-api-key"     # Windows
Run the assistant

bash
Copy
Edit
python assistant/main.py
🔐 Optional Features You Can Add
Email and calendar access (with imaplib, Google API)

Wake word detection

GUI interface (Tkinter/PyQt)

Smart routines and reminders

Multilingual voice support

📸 Demo
First image is a GUI
![A1](https://github.com/user-attachments/assets/147e6d03-dd4f-4bc5-afeb-89d054b5082d)
Second immage is Command Output Open youtube
![A3](https://github.com/user-attachments/assets/aa4ea8ff-449a-47aa-a4e8-3ef82cc400b9)


🙋 Author
Anurag Yadav
📎 GitHub

📄 License
This project is licensed under the MIT License.
    
