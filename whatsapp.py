import pyttsx3 # type: ignore
import time
import pyautogui # type: ignore

# Initialize the text-to-speech engine
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)  # Change to `voice`, not `voices`
engine.setProperty('rate', 170)

# Function to make the assistant speak
def speak(audio):
    engine.say(audio)
    engine.runAndWait()

# Function to send a WhatsApp message
def sendMessages():
    try:
        speak("Whom do you want to send a message to, my princess?")
        recipient = input("Enter the name: ")
        
        speak("What do you want to say, highness?")
        message = input("Enter the message, angel: ")
        
        speak("Are you ready to send the message, princess?")
        confirmation = input("Have you done, princess (yes/no)? ").lower()
        
        if confirmation == "yes":
            # Open WhatsApp
            pyautogui.press("win")  # On Windows, this opens the start menu
            time.sleep(2)
            pyautogui.typewrite("WhatsApp")
            time.sleep(2)
            pyautogui.press("enter")
            time.sleep(5)  # Wait for WhatsApp to open
            
            # Search for the recipient
            pyautogui.typewrite(recipient)
            time.sleep(2)
            pyautogui.press("down")  # Navigate to the recipient
            time.sleep(1)
            pyautogui.press("enter")
            time.sleep(1)
            
            # Type and send the message
            pyautogui.typewrite(message)
            time.sleep(1)
            pyautogui.press("enter")
            speak("The message has been sent, my princess.")
        
        else:
            speak("Alright, let's do it again.")
    
    except Exception as e:
        speak("An error occurred while sending the message.")
        print(f"Error: {e}")

# Run the function
if __name__ == "__main__":
    sendMessages()
