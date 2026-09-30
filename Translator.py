from time import sleep
from googletrans import Translator
from gtts import gTTS 
import googletrans 
import pyttsx3 
import speech_recognition as sr
import os
from playsound import playsound 
import time

# Initialize the speech engine
engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[1].id)  # Changed to voices[1] (female voice in many setups)
engine.setProperty('rate', 170)


# Function to speak out text
def speak(audio):
    engine.say(audio)
    engine.runAndWait()


# Function to capture microphone input
def takeCommand():
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
        speak("Say that again please.")
        print("Say that again please...")
        return "None"
    
    return query


# Function to translate spoken text into another language
def translate(query):
    speak("Sure highness")
    print(googletrans.LANGUAGES)
    translator = Translator()
    
    speak("Choose the language in which you want to translate")
    a = input("Enter the language code (e.g., 'fr' for French, 'es' for Spanish): ").lower()
    
    try:
        # Translate the input query
        text_to_translate = translator.translate(query, src="auto", dest=a)
        translated_text = text_to_translate.text
        print(f"Translated text: {translated_text}")
        
        # Convert the translated text to speech
        speakgl = gTTS(text=translated_text, lang=a, slow=False)
        speakgl.save("voice.mp3")
        
        # Play the generated voice file
        playsound("voice.mp3")

        # Wait and delete the voice file to keep things clean
        time.sleep(5)
        os.remove("voice.mp3")

    except Exception as e:
        print(f"Unable to translate. Error: {e}")
        speak("I am unable to translate at the moment.")

