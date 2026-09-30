# AI DAVID
import pyttsx3
import speech_recognition as sr 
import requests 
from bs4 import BeautifulSoup 
import datetime
import os       
import pyautogui
import webbrowser
from time import sleep
import random
import tkinter as tk
from tkinter import messagebox
from tkinter.ttk import Button
from keyboard import Volume_Up
import speedtest
import pyjokes
from schedule import stop_reminders  # Import the stop function from schedule.py

engine= pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
engine.setProperty("voices" , voices[1].id)
engine.setProperty('rate',170)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def takeCommand(): 
    #It takes microphone input from the user and returns string output
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        r.energy_threshold = 300
        audio = r.listen(source)
 
    try:
        print("Recognizing...")    
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")
        

    except Exception as e:
        # print(e)
        speak("say that again please")    
        print("Say that again please...")  
        return "None"
    return query

def get_command():
    """Get command based on the current mode."""
    if mode == "1":  # Voice mode
        return takeCommand().lower() # type: ignore
    elif mode == "2":  # Manual mode
        return input("Enter your command: ").lower()
    else:
        return None

if __name__ == "__main__":
    print("Select mode: 1 for Voice, 2 for Manual")
    speak("Select mode: Press 1 for Voice mode or 2 for Manual mode")
    mode = input("Enter mode (1/2): ").strip()

    def process_command(query):
        global mode  # Allow mode to be updated dynamically
        if query:  # Ensure query is not empty
            # Mode switching logic
            if "switch to voice mode" in query:
                speak("Switching to voice mode.")
                print("Switching to voice mode.")
                mode = "1"
                return True
            elif "switch to manual mode" in query:
                speak("Switching to manual mode.")
                print("Switching to manual mode.")
                mode = "2"
                return True

            if "quiet" in query or "silent" in query or "silence" in query:
                speak("yes your Highness, But you can call me anytime")
                return False  # Exit the inner loop

            # NORMAL TALK WITH DAVID
            elif "hello" in query:
                print("hello princess, how are you 🥰🥰")   
                speak("hello princess, how are you")   
            elif "i am " in query:
                print("thats great your highness 👍🏻😊")
                speak("thats great your highness")
            elif "how are you" in query:
                print("all good angel, thank you to ask me.🤗🤗")
                speak("all good angel, thank you to ask me.")
            elif "are you" in query:
                print("yes because of you princess🙃🙃")
                speak("yes because of you princess")
            elif "can you" in query:
                print("sure, your highness 😃😉") 
                speak("sure, your highness")          
            elif "thank you" in query or "thanks" in query:
                speak("Anytime your Highness.")
                print("Anytime your Highness.😇😇")
            elif "will you" in query:
                print("yes of course, if you want, so i can my princess 😍😍")
                speak("yes of course, if you want, so i can my princess ")   
            elif "I love you" in query:
                print("I love you too princess 💖💗")
                speak("I love you too princess ")
            elif "no it's not" in query:
                print("I apologize to you princess 🥺🥹🥲")
                speak("I apologize to you princess")
            elif"bore" in query or "boring" in query:
                print("Tell me princess, how can I entertain you, can i play music or you wanna play a game with me and if you want so i can tell you a good joke 🙃🙃 ")
                speak("Tell me princess, how can I entertain you, can i play music or you wanna play a game with me and if you want so i can tell you a good joke ")

            # MY FAVOURITE SONG
            elif "tired" in query or "music" in query:
                speak("wait i am doing something intersted for you ")
                print("wait i am doing something intersted for you 🧐🤔")
                a = (1,2,3)
                b = random.choice(a)
                if b == 1:
                    webbrowser.open(input())
                elif b == 2:
                        webbrowser.open("https://www.youtube.com/watch?v=NMmquUVy0MQ&list=RDGMEMCMFH2exzjBeE_zAHHJOdxgVMNMmquUVy0MQ&start_radio=1")
                elif b == 3:
                    webbrowser.open("https://www.youtube.com/watch?v=caoGNx1LF2Q&list=RDcaoGNx1LF2Q&start_radio=1")

            # YOUTUBE VIDEO CONTROLER
            elif "pause" in query:
                pyautogui.press("k")
                print("done princess 👍🏻😊")
                speak("done princess ")
               
            elif "play" in query:
                pyautogui.press("k")
                print("done princess")
                speak("done princess")
                
            elif "mute" in query:
                pyautogui.press("m")
                print("done princess 👍🏻😊")
                speak("done princess")

            # VOLUME CONTROLER
                
            elif "increase volume" in query:    
                from keyboard import Volume_Up
                Volume_Up()
                print("increaseing..... 👍🏻😊")
                speak("increaseing.....")
                

            elif "decrease volume" in query:
                from keyboard import Volume_Down
                Volume_Down()
                print("decreaseing.... 👎🏻😊")
                speak("decreaseing....")

            # BRIGHTNESS CONTOLLER
            elif "increase brightness" in query:
                from keyboard import brightness_up
                brightness_up()
                print("increaseing..... 👍🏻😊")
                speak("increaseing.....")
                
            elif "decrease brightness" in query:
                from keyboard import brightness_down
                brightness_down()
                print("decreaseing.... 👎🏻😊")
                speak("decreaseing....")

            # OPEN AND CLOSE APPS
            elif "open" in query:
                print("as you say your highness 🫡🫡")
                speak("as you say your highness")                
                query = query.replace("open","")
                query = query.replace("david","")
                pyautogui.press("super")
                pyautogui.typewrite(query)
                pyautogui.press("enter")
                print("this is you said princess 🤨🤨")
                speak("this is you said princess")
                
            elif "yes" in query:
                pyautogui.press("enter")
                pyautogui.press("space")
                print("thank you for confirming me angel 😊😊")
                speak("thank you for confirming me angel")
                

            elif "close" in query:
                pyautogui.hotkey('alt', 'f4')
                print("as you say your highness 🫡🫡")
                speak("as you say your highness")

            elif "split" in query:
                pyautogui.hotkey("alt","tab")
                print("done princess 👍🏻😊")
                speak("done princess")
            
            # SCREENSHOT AND CAMERA
            elif "screenshot" in query:
                # Create a "Screenshots" folder if it doesn't exist
                screenshot_folder = "Screenshots"
                os.makedirs(screenshot_folder, exist_ok=True)
                
                # Generate a unique filename with a timestamp
                filename = f"{screenshot_folder}/screenshot_{datetime.datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}.png"
                
                # Take a screenshot and save it
                im = pyautogui.screenshot()
                im.save(filename)
                
                print(f"📸 Screenshot saved as: {filename}")

            elif "photo" in query:
                pyautogui.press("super")
                pyautogui.typewrite("camera")
                pyautogui.sleep(2.0)
                pyautogui.press("enter")
                pyautogui.sleep(2.0)
                speak("princess smile")
                pyautogui.press("enter")

            # INTERNET SURFING
            elif "google" in query:
                from InternetSurfing import search_google
                search_google(query)
            elif "youtube" in query:
                from InternetSurfing import search_youtube
                search_youtube(query)
            elif "wikipedia" in query:
                from InternetSurfing import search_wikipedia
                search_wikipedia(query)

            # CURRENT TIME
            elif "the time" in query:
                strTime = datetime.datetime.now().strftime("%H:%M:%S")    
                print(f"princess, the time is {strTime} ⌚🧐")
                speak(f"princess, the time is {strTime}")
                
            # REMEMBER FUNCTION
            elif "remember that" in query: 
                RM = query.replace("remember that","")
                RM = query.replace("david", "")
                speak("yes your highness , you told me to " + RM)
                remember = open("Remember" , "w")
                remember.write(RM)
                remember.close()
            
            elif " what do you remember" in query:
                remember = open("Remember", "r")
                speak("princes, you told me to " + remember.read())

            # WHATSAPP 
            elif "send message" in query:
                from whatsapp import sendMessages
                sendMessages()

            # GAME PLAY 
            elif "game" in query:
                from GamePlay import Fun
                speak("I waiting to play with you Angel,lets Start the game...")
                print("I waiting to play with you Angel 😊😊, lets Start the game...")
                Fun()  # This will call the game function from GamePlay.py
                
            elif "exit" in query:
                print("Exiting the assistant...")
                speak("Exiting the assistant...")
                return False

            # SHUTDOWN SYSTEM
            elif "shutdown" in query:
                speak("are you sure you wanna shutdown Angel")
                shutdown = input("Lets Confirm It 🤨🤨: ")
                if shutdown == "yes":
                    os.system("shutdown /s /t 1")
                else:
                    return True

            # FILE MANAGER 
            elif "manage" in query:
                from FileManager import FileManager
                speak("sure princess, please enter your path here")
                FileManager()

            # INTERNET SPEED TESTING
            elif "internet speed" in query:
                wifi = speedtest.Speedtest()
                upload_net = round(wifi.upload() / 1048576, 2)  # Convert bytes to Megabytes
                download_net = round(wifi.download() / 1048576, 2)

                print("wifi upload speed is: ",upload_net)
                print("wifi download speed is; ",download_net)
                speak(f"princess your wifi upload speed is{upload_net}  megabits per second.")
                speak(f"and your wifi download speed is{download_net}  megabits per second.")

            # JOKES
            elif "joke" in query:
                joke = pyjokes.get_joke()
                speak(joke)
                print(joke)

            # DAVID TRANSLATOR
            elif "translate" in query:
                from Translator import translate
                query = query.replace("Scorpio","")
                query = query.replace("translate","")
                translate(query)
                
            # SCHEDULE FIXER
            from schedule import set_schedule, my_schedule, check_reminders

            if "set schedule" in query:
                set_schedule()
            elif "my schedule" in query:
                my_schedule()
                check_reminders()

            elif "news" in query:
                speak("today latest news is: <news>")
                print("today latest news is: <news>")
                


            # EXIT COMMAND

            elif "bye" in query or "sleep" in query or "exit" in query:
                query = query.replace("david","")
                print("bye bye👋🏻👋🏻 Princess ,david🙋🏻🙋🏻 miss you😢😭")
                speak("bye bye Princess ,david miss you")
                exit()
            return True  # Continue the inner loop

            


    while True:
        query = get_command()
        if query and "david" in query:
            from GreetMe import WishMe
            WishMe()

            while True:
                query = get_command()
                if not process_command(query):
                    break

    # Ensure graceful exit
    stop_reminders()


