import os
import pyttsx3
import speech_recognition as sr
from plyer import notification
from datetime import datetime
import time
import threading

stop_reminder_thread = False  # Flag to stop the reminder thread

def speak(audio):
    """Text-to-speech function"""
    engine = pyttsx3.init("sapi5")
    voices = engine.getProperty("voices")
    engine.setProperty("voices", voices[1].id)
    engine.setProperty('rate', 170)
    engine.say(audio)
    engine.runAndWait()

def takeCommand():
    """Takes voice input from the user and returns recognized text"""
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
        return query.lower()
    except Exception:
        speak("Say that again, please.")
        return "None"

def set_schedule():
    """Sets a new schedule with time-based alerts"""
    speak("Highness, do you want to clear your old tasks? Please speak yes or no.")
    query = takeCommand()

    if "yes" in query:
        open("tasks.txt", "w").close()  # Clear file
        speak("Old tasks cleared, Highness.")
    
    speak("How many tasks would you like to add?")
    try:
        no_tasks = int(input("ENTER NUMBER OF TASKS: "))  # Task count
    except ValueError:
        speak("Sorry, I didn't understand. Please enter a number.")
        return
    
    with open("tasks.txt", "a") as file:
        for i in range(no_tasks):
            speak(f"Please speak your task {i + 1}.")
            task_item = takeCommand()
            if task_item == "none":
                continue
            
            while True:
                speak(f"Please speak the time for this task in hours and minutes.")
                time_task = input(f"ENTER TIME FOR TASK {i + 1} (HH:MM AM/PM): ")  # Manual input for precise format
                
                # Validate time format
                try:
                    datetime.strptime(time_task, "%I:%M %p")
                    break  # Valid format
                except ValueError:
                    speak("Invalid time format. Please try again.")

            file.write(f"{time_task} - {task_item}\n")
            speak(f"Task {i + 1} added: {task_item} at {time_task}")

    speak("Your schedule has been saved successfully, Highness!")

def my_schedule():
    """Reads the schedule and announces tasks via notification & voice."""
    if not os.path.exists("tasks.txt") or os.stat("tasks.txt").st_size == 0:
        speak("Highness, you don't have any tasks in your schedule.")
        return

    with open("tasks.txt", "r") as file:
        content = file.readlines()

    if content:
        message = "".join(content)
        notification.notify(
            title="My Schedule:",
            message=message,
            timeout=25  # Notification stays for 25 seconds
        )

        # Speak each task one by one
        for task in content:
            speak(task.strip())

    else:
        speak("Highness, your schedule is empty.")

def validate_task_format(task):
    """Validate and split task into time and description."""
    if " - " not in task:
        return None, None
    try:
        task_time, task_desc = task.split(" - ", 1)
        datetime.strptime(task_time, "%I:%M %p")  # Validate time format
        return task_time, task_desc
    except ValueError:
        return None, None

def check_reminders():
    """Continuously checks time for scheduled reminders."""
    global stop_reminder_thread
    while not stop_reminder_thread:
        now = datetime.now().strftime("%I:%M %p")  # Current time in HH:MM AM/PM format
        
        if os.path.exists("tasks.txt"):
            with open("tasks.txt", "r") as file:
                tasks = file.readlines()

            for task in tasks:
                task = task.strip()
                task_time, task_desc = validate_task_format(task)
                if not task_time or not task_desc:
                    print(f"Skipping invalid task: {task}")
                    continue

                if task_time == now:
                    notification.notify(
                        title="Reminder ⏰",
                        message=f"Time for: {task_desc}",
                        timeout=10
                    )
                    speak(f"Princess, it's time for {task_desc}")

        time.sleep(60)  # Check every minute

# Start reminder checking in the background
reminder_thread = threading.Thread(target=check_reminders, daemon=True)
reminder_thread.start()

# Add this to stop the thread gracefully when the program exits
def stop_reminders():
    global stop_reminder_thread
    stop_reminder_thread = True
