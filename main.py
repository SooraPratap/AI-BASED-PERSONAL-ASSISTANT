
import pyttsx3
import speech_recognition 
import datetime
import wikipedia
import webbrowser
import os
import getpass
from bs4 import BeautifulSoup

import smtplib

import requests
import random
#import speedtest
import pyaudio
#import schedule
import time

import sys


#for i in range(3):
  #  a = getpass.getpass("Enter Password to open buddy :-  ")
  #  pw_file = open("password.txt","r")
   # pw = pw_file.read()
   # pw_file.close()
   # if (a==pw):
   #     print("WELCOME SIR ! PLZ SPEAK [WAKE UP] TO LOAD ME UP")
    #    break
    #elif (i==2 and a!=pw):
    #    exit()

    #elif (a!=pw):
    #    print("Try Again")


#from INTRO import play_gif
#play_gif

engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[0].id)
rate = engine.setProperty("rate",170)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def takeCommand():
    r = speech_recognition.Recognizer()
    with r as source:
        print("Listening.....")
        r.pause_threshold = 1
        r.energy_threshold = 300
        audio = r.listen(source,0,4)

    try:
        print("Understanding..")
        query  = r.recognize_google(audio,language='en-in')
        print(f"You Said: {query}\n")
    except Exception as e:
        print("Say that again")
        return "None"
    return query


if __name__ == "__main__":
    while True:
        query = takeCommand().lower()
        if "wake up" in query:
            from GreetMe import greetMe
            greetMe()

            while True:
                query = takeCommand().lower()
                if "go to sleep" in query:
                    speak("Ok sir , You can me call anytime")
                    break 

                elif "hello" in query:
                    speak("Hello sir, how are you ?")
                elif "i am fine" in query:
                    speak("that's great, sir")
                elif "how are you" in query:
                    speak("Perfect, sir")
                elif "thank you" in query:
                    speak("you are welcome, sir")
                 
                elif "change password" in query:
                    speak("What's the new password")
                    new_pw = input("Enter the new password\n")
                    new_password = open("password.txt","w")
                    new_password.write(new_pw)
                    new_password.close()
                    speak("Done sir")
                    speak(f"Your new password is{new_pw}")

                elif 'play music' in query:
                    music_dir = 'c:\\Users\\abhay\\Music'
                    songs = os.listdir(music_dir)
                    #print(songs)    
                    os.startfile(os.path.join(music_dir, songs[1]))

                elif "tired" in query:
                    speak("Playing your favourite songs, sir")
                    a = (1,2) 
                    b = random.choice(a)
                    if b==1:
                        webbrowser.open("https://www.youtube.com/watch?v=6GxXehkPyBs&list=RD6GxXehkPyBs&start_radio=1")
                    if b==2:
                        webbrowser.open("https://www.youtube.com/watch?v=6GxXehkPyBs&list=RD6GxXehkPyBs&start_radio=1")

                elif "set an alarm" in query:
                    print("input time example:- 10 and 10 and 10")
                    speak("Set the time")
                    a = input("Please tell the time :- ")
                    alarm(a)
                    speak("Done,sir")
                
                
                

                elif "volume up" in query:
                    from keyboard import volumeup
                    speak("Turning volume up,sir")
                    volumeup()
                elif "volume down" in query:
                    from keyboard import volumedown
                    speak("Turning volume down, sir")
                    volumedown()

                elif "whatsapp" in query:
                    from Whatsapp import sendMessage
                    sendMessage()


                elif "google" in query:
                  from SearchNow import searchGoogle
                  searchGoogle(query)
                elif "youtube" in query:
                    from SearchNow import searchYoutube
                    searchYoutube(query)
                elif "wikipedia" in query:
                    from SearchNow import searchWikipedia
                    searchWikipedia(query)

                

               

                
                elif "focus mode" in query:
                    a = int(input("Are you sure that you want to enter focus mode :- [1 for YES / 2 for NO "))
                    if (a==1):
                        speak("Entering the focus mode....")
                        os.startfile("C:\\AI Personal Assistant\\FocusMode.py")
                        exit()

                    
                    else:
                        pass

                elif "remember that" in query:
                    rememberMessage = query.replace("remember that","")
                    rememberMessage = query.replace("buddy","")
                    speak("You told me to remember that"+rememberMessage)
                    remember = open("Remember.txt","a")
                    remember.write(rememberMessage)
                    remember.close()
                elif "what do you remember" in query:
                    remember = open("Remember.txt","r")
                    speak("You told me to remember that" + remember.read())

                elif "temperature" in query:
                    place = input("Enter the name of Place:")
                    search = f"Weather in {place}"
                    url = f"https://www.gooogle.com/search?&q={search}"
                    r = requests.get(url)
                    soup = BeautifulSoup(r.text, "html.parser")
                    update = soup.find("div", class_="BNeawe").text
                    print(f"{search} now is {update}")
                    
                elif "the time" in query:
                    strTime = datetime.datetime.now().strftime("%H:%M")    
                    speak(f"Sir, the time is {strTime}")

                
                elif "open" in query:
                    from Dictapp import openappweb
                    openappweb(query)
                elif "close" in query:
                    from Dictapp import closeappweb
                    closeappweb(query)

                elif "schedule my day" in query:
                    tasks = []  
                    speak("Do you want to clear old tasks (Plz speak YES or NO)")
                    query = takeCommand().lower()
                    if "yes" in query:
                        file = open("tasks.txt","w")
                        file.write(f"")
                        file.close()
                        no_tasks = int(input("Enter the no. of tasks :- "))
                        i = 0
                        for i in range(no_tasks):
                            tasks.append(input("Enter the task :- "))
                            file = open("tasks.txt","a")
                            file.write(f"{i}. {tasks[i]}\n")
                            file.close()
                    elif "no" in query:
                        i = 0
                        no_tasks = int(input("Enter the no. of tasks :- "))
                        for i in range(no_tasks):
                            tasks.append(input("Enter the task :- "))
                            file = open("tasks.txt","a")
                            file.write(f"{i}. {tasks[i]}\n")
                            file.close()

                elif "show my schedule" in query:
                    file = open("tasks.txt","r")
                    content = file.read()
                    file.close()
                

                elif "show my focus" in query:
                    from FocusGraph import focus_graph
                    focus_graph()

                elif "restart the system" in query:
                    os.system("shutdown /r /t 5")
               
                elif "go to sleep" in query:
                    speak(' alright then, I am switching off')
                    sys.exit()

                

                w
                        