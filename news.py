from GoogleNews import GoogleNews  # type: ignore
import speech_recognition as sr
import pyttsx3


googleNews = GoogleNews()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)  # Set to the first
recognizer = sr.Recognizer()

def fetch_news():
    with sr.Microphone() as source:
        print("Listening for news...")
        audio = recognizer.listen(source)

    try:
        query = recognizer.recognize_google(audio)
        print(f"You said: {query}")
        if "news" in query:
            googleNews.get_news("latest")
            news = googleNews.results()
            for item in news:
                engine.say(item['title'])
            engine.runAndWait()
            return news
    except Exception as e:
        print("Sorry, I couldn't fetch the news.")
        engine.say("Sorry, I couldn't fetch the news.")
        engine.runAndWait()
        return None