import speech_recognition as sr
import pyttsx3 
import wikipedia
import webbrowser
import pywhatkit

# Initialize Speech Engine
engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[1].id)
engine.setProperty('rate', 170)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def takeCommand():
    """Takes microphone input from the user and returns a string output."""
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

    except Exception as e:
        speak("Say that again, please.")    
        print("Say that again, please...")  
        return "none"

def search_google(query):
    if "google" in query:
        query = query.replace("david", "").replace("open google", "").replace("search google", "").strip()
        speak("As you said, searching Google...")
        
        try:
            pywhatkit.search(query) 
            result = wikipedia.summary(query, sentences=1)
            speak("Here is what I found:")
            print(result)
            speak(result)
        except wikipedia.exceptions.DisambiguationError:
            speak("There are multiple results. Please be more specific.")
        except wikipedia.exceptions.PageError:
            speak("No relevant Wikipedia page found.")
        except Exception:
            speak("I couldn't find anything relevant.")

def search_youtube(query):
    if "youtube" in query:
        speak(f"Searching YouTube for {query}")
        query = query.replace("open youtube", "").replace("search youtube", "").replace("david", "").strip()
        web = f"https://www.youtube.com/results?search_query={query}"
        webbrowser.open(web)
        pywhatkit.playonyt(query)
        speak("Here are the YouTube results.")

def search_wikipedia(query):
    if "wikipedia" in query:
        speak(f"Searching Wikipedia for {query}...")
        query = query.replace("wikipedia", "").replace("search wikipedia", "").replace("david", "").strip()
        
        try:
            result = wikipedia.summary(query, sentences=2)
            print(result)
            speak("According to Wikipedia...")
            speak(result)
        except wikipedia.exceptions.DisambiguationError as e:
            speak("There are multiple results. Please be more specific.")
        except wikipedia.exceptions.PageError:
            speak("No Wikipedia page found for the given search.")

if __name__ == "__main__":
    query = takeCommand()
    if query != "none":
        if "google" in query:
            search_google(query)
        elif "youtube" in query:
            search_youtube(query)
        elif "wikipedia" in query:
            search_wikipedia(query)
        else:
            speak("I am not sure how to help with that.")
