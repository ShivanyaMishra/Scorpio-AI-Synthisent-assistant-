import os
import shutil
import pyttsx3
import json
from time import time

# Initialize Text-to-Speech
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)  # male voice
engine.setProperty('rate', 170)  # Speed

def speak(audio):
    """Speaks the given text."""
    engine.say(audio)
    engine.runAndWait()

def FileManager():
    """Organizes files in a directory by their extensions and logs changes."""
    path = input("Enter your path: ")

    # Track the start time
    start_time = time()

    if not os.path.exists(path):
        speak("The specified path does not exist.")
        print("The specified path does not exist.")
        return

    # List files in the directory
    files = os.listdir(path)
    
    if not files:
        speak("The directory is empty.")
        print("The directory is empty.")
        return

    moved_files = {}
    total_files = 0

    for file in files:
        file_name, extension = os.path.splitext(file)
        extension = extension[1:]  # Remove the dot from the extension

        if not extension:  # Skip files without an extension
            continue

        folder_path = os.path.join(path, extension)

        if not os.path.exists(folder_path):
            os.makedirs(folder_path)

        source_file = os.path.join(path, file)
        destination_file = os.path.join(folder_path, file)

        try:
            shutil.move(source_file, destination_file)
            moved_files[file] = folder_path  # Log moved files
        except Exception as e:
            print(f"Error moving {file}: {str(e)}")

        total_files += 1  

    # Save log file for undo option
    log_file = os.path.join(path, "file_log.json")
    with open(log_file, "w") as f:
        json.dump(moved_files, f)

    # Track the end time
    end_time = time()
    elapsed_time = end_time - start_time

    speak(f"Princess, your files are organized. {len(moved_files)} files moved in {elapsed_time:.2f} seconds.")
    print(f"File organization complete. {len(moved_files)} files moved in {elapsed_time:.2f} seconds.")

def UndoLastMove():
    """Restores files to their original locations using the log file."""
    path = input("Enter your path where files were organized: ")
    log_file = os.path.join(path, "file_log.json")

    if not os.path.exists(log_file):
        speak("No previous move log found. Undo operation not possible.")
        print("No previous move log found. Undo operation not possible.")
        return

    with open(log_file, "r") as f:
        moved_files = json.load(f)

    for file, folder in moved_files.items():
        source = os.path.join(folder, file)
        destination = os.path.join(path, file)

        try:
            shutil.move(source, destination)
        except Exception as e:
            print(f"Error restoring {file}: {str(e)}")

    # Remove log file after undo
    os.remove(log_file)

    speak(f"Princess, undo operation complete. Files are restored to their original location.")
    print("Undo operation complete. Files restored.")

if __name__ == "__main__":
    while True:
        print("\n1. Organize Files")
        print("2. Undo Last Move")
        print("3. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            FileManager()
        elif choice == "2":
            UndoLastMove()
        elif choice == "3":
            speak("Goodbye, Princess! Have a great day! ")
            break
        else:
            print("Invalid choice! Please try again.")
            speak("Invalid choice! Please try again.")