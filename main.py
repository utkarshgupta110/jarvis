import speech_recognition as sr
import webbrowser
import pyttsx3
import musicLibrary
import os
import subprocess
from whatsapp import send_msg
from news import get_news

recognizer = sr.Recognizer()

def speak(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

def microphone(flag = 0):
    with sr.Microphone() as source:
        # Listen for command after awekening
        if flag == 0:
            print("Listening.......")
            audio = recognizer.listen(source, timeout=100, phrase_time_limit=4)
        elif flag == 1:
            print("Recognizing.......")
            audio = recognizer.listen(source, timeout=25, phrase_time_limit=4)
        else :
            print("Speak message to be sent")
            audio = recognizer.listen(source, timeout=25, phrase_time_limit=4)
        
    command = recognizer.recognize_google(audio)
    return command

def processCommand(command):
    command = command.lower()

    if "open google" in command:
        webbrowser.open("https://www.google.com")

    elif "open poki games"  in command:
        webbrowser.open("https://poki.com/en/g/subway-surfers")

    elif "open github"  in command:
        webbrowser.open("https://github.com/utkarshgupta110")

    elif "linkedin" in command:
        webbrowser.open("http://www.linkedin.com/in/utkarsh-gupta-700248259")

    elif command.startswith("play"):
        song = command.split(" ")[1]
        link = musicLibrary.music[song]
        webbrowser.open(link)

    elif "open desktop" in command:
        path = r"C:\Users\Utkarsh Gupta\OneDrive\Desktop"
        os.startfile(path)

    # open downloads folder
    elif "open youtube" in command:
        path = r"C:\Users\Utkarsh Gupta\OneDrive\Desktop\YouTube.lnk"
        os.startfile(path)

    # open vs code
    elif "open vscode" in command:
        code_path = r"C:\Users\Utkarsh Gupta\AppData\Local\Programs\Microsoft VS Code\Code.exe"
        os.startfile(code_path)

    # open camera (windows camera)
    elif "open camera" in command:
        subprocess.run("start microsoft.windows.camera:", shell=True)
    
    elif "open whatsapp" in command:
        os.startfile("shell:AppsFolder\\5319275A.WhatsAppDesktop_cv1g1gvanyjgm!App")
        command = microphone(2)
        send_msg(command)

    elif "give me news" in command:
        data = get_news()
        speak(data)

    else:
        print("Command not found")
        
if __name__ == "__main__":
    speak("Initiailizing Jarvis.......")
    # Lesson for the wake world "Jarvis" 

    # Obtain audio from the microphone
    while True:
        try:
            command = microphone()
            if(command.lower() == "hi jarvis"):
                speak("Yes i am active ")
            command = microphone(1)
            if(command.lower() == "stop"):
                speak("jarvis is terminated")
                break
            processCommand(command)
        except Exception as e:
            print("Error; {0}".format(e))