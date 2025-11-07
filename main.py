from Agent import *
from Listen import listen
from Speak import speak

def main():
    while True:
        command = listen()
        print(f"User said: {command}")
        if command.lower() in ["exit", "quit", "stop"]:
            speak("Goodbye!")
            break
        

        full_response = response(command)
        text, _ = code_seprator(full_response)

        # Print the full response (text + code as returned by Jarvis)
        print(f"\nAgent full response:\n{full_response}\n")

        # Speak only the textual part
        speak(text)

if __name__ == "__main__":
    main()
