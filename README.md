# 🤖 Jarvis Voice Assistant (Python AI Desktop Assistant)

Jarvis is a Python-based AI voice assistant that can perform daily desktop tasks using voice commands.  
It can open applications, play music, send WhatsApp messages, fetch news, and control system operations.

This project is built for **learning, personal use, and placement portfolio demonstration**.

## Features
- Voice command recognition
- Natural language processing
- Integration with smart home devices
- Task management capabilities
- Information retrieval from the web

## Installation Instructions
1. **Clone the repository**:
   ```bash
   git clone https://github.com/utkarshgupta110/jarvis.git
   cd jarvis
   ```
2. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```
3. **Run the assistant**:
   ```bash
   python jarvis.py
   ```
---

# 🚀 Features

### 🎤 Voice Activation
- Wake word: **"Hi Jarvis"**
- Speech recognition using microphone
- Text-to-speech response

### 🌐 Web & Browser Control
- Open Google
- Open GitHub
- Open LinkedIn
- Open YouTube
- Open custom websites

### 💻 System Automation
- Open Desktop folder
- Open VS Code
- Open Camera
- Open any application via path

### 🎵 Music Player
- Play songs from custom music library
- Opens songs directly in browser

### 💬 WhatsApp Automation
- Opens WhatsApp Desktop
- Sends message using voice command

### 📰 News Feature
- Fetches latest news
- Speaks top headlines

---

# 🛠️ Tech Stack

- Python 3
- SpeechRecognition
- pyttsx3 (Text to speech)
- PyWhatKit (WhatsApp automation)
- Requests (News API)
- Webbrowser
- OS & Subprocess (system control)

---

# 📦 Installation & Setup

## 1️⃣ Clone repository
```bash
git clone https://github.com/utkarshgupta110/jarvis.git
cd jarvis
```

## 2️⃣ Install dependencies
```bash
pip install speechrecognition
pip install pyttsx3
pip install pywhatkit
pip install requests
pip install pyaudio
```

If pyaudio error:
```bash
pip install pipwin
pipwin install pyaudio
```

---

# ▶️ Run Jarvis
```bash
python main.py
```

Say:
```
Hi Jarvis
```

Then give commands.

---

# 🧠 Available Voice Commands

### 🌐 Web Commands
- Open Google  
- Open GitHub  
- Open LinkedIn  
- Open YouTube  

### 💻 System Commands
- Open desktop  
- Open VS code  
- Open camera  

### 🎵 Music
```
play songname
```

### 💬 WhatsApp
```
open whatsapp
```
Then speak message.

### 📰 News
```
give me news
```

### 🛑 Stop Jarvis
```
stop
```

---

# 📁 Project Structure
```
jarvis/
│── main.py
│── musicLibrary.py
│── whatsapp.py
│── news.py
│── README.md
│── .gitignore
```

---

# 🔐 Security Note
- This project runs locally on your system
- No personal data is collected
- No remote access is given
- Do not upload API keys publicly

---

# 🎯 Future Improvements
- ChatGPT integration
- GUI interface (Iron Man style)
- Face recognition login
- Smart home automation
- Advanced AI conversation

---

# 👨‍💻 Author
**Utkarsh Gupta**  
B.Tech CSE (AI & Data Science)

GitHub:  
https://github.com/utkarshgupta110

---

# ⭐ Support
If you like this project:
- Star ⭐ the repo
- Use it in portfolio
- Improve and build your own AI assistant

## Contributing
Feel free to enhance the project by submitting a pull request with your features, bug fixes, or improvements.

## License
This project is licensed under the MIT License.
