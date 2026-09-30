# GREET ME ZIRA

import datetime
import pyttsx3 # type: ignore

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voices',voices[1].id)
engine.setProperty('rate',170)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def WishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("hi, good morning Highness")
        print("hi, good morning Highness😊😊")

    elif hour >= 12 and hour < 18:
        speak("hi, good afternoon Angel")
        print("hi, good afternoon Angel🙃🙃")
    else:
        speak("hi, good evening princess")
        print("hi, good evening princess😄😄")

    speak("I AM DAVID HOW CAN I HELP YOU")
    print("I AM DAVID🙋🏻 HOW CAN I HELP YOU.....")

