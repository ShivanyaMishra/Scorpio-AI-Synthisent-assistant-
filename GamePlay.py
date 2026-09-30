import pyttsx3 # type: ignore
import random

# Initialize the speech engine
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voices', voices[1].id)
engine.setProperty('rate', 170)

def speak(audio):
    """Text-to-Speech function"""
    engine.say(audio)
    engine.runAndWait()

def Fun():
    speak("I LIKE TO PLAY WITH YOU, MY ANGEL")

    while True:
        # Display options to the user
        print("\nChoose one 🤫:\n R = Stone 🪨\n P = Paper 📄\n S = Scissor ✂️")
        speak("Choose one, R for Stone, P for Paper, or S for Scissor")

        # Game choices
        options = {'r': 'stone', 'p': 'paper', 's': 'scissor'}
        user_choice = input("ENTER YOUR CHOICE (R/P/S): ").lower()

        # Validate user input
        if user_choice not in options:
            print("Please enter a valid choice 💝🤗")
            speak("Please enter a valid choice, princess")
            continue

        computer_choice = random.choice(list(options.values()))  # Computer's random choice

        # Announce choices
        print(f"You chose 🙃🙃 : {options[user_choice]}")
        speak(f"You chose {options[user_choice]}")
        print(f"Computer chose 😋😋 : {computer_choice}")
        speak(f"I am going to choose {computer_choice}, your highness")

        # Determine the winner
        if options[user_choice] == computer_choice:
            print("Oops! It's a tie, angel 🤗🤗")
            speak("Oops! It's a tie, angel")
        elif (options[user_choice] == 'stone' and computer_choice == 'scissor') or \
             (options[user_choice] == 'paper' and computer_choice == 'stone') or \
             (options[user_choice] == 'scissor' and computer_choice == 'paper'):
            print("You win, princess! 🥰😍")
            speak("You win, princess!")
        else:
            print("David wins! 🥲😭")
            speak("David wins! Better luck next time, princess!")

        # Ask if the player wants to play again
        print("\nDO YOU WANT TO PLAY AGAIN? Y🤩 / N😥")
        speak("Do you want to play again? Say yes or no.")
        ans = input("Enter your answer (Y/N): ").lower()

        if ans == 'n':
            break

    print("THANKS FOR PLAYING 💖💗")
    speak("Thanks for playing with me, princess!")

if __name__ == "__main__":
    Fun()
