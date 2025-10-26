import pyttsx3
import speech_recognition as sr
from transformers.pipelines import pipeline
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty("voice", voices[0].id)


def speak(text):
    engine.say(text)
    engine.runAndWait()

def listen():
    r = sr.Recognizer()
    with sr.Microphone as source:
        print("Listening ...")
        r.adjust_for_ambient_noise(source)
        audio = r.listen()
        try:
            print("Recognizing ...")
            text = r.recognize_google(audio)
            print(f"You: {text}")
        except Exception as e:
            print(f"Error Details: {e}")
            speak("An Error Occured. Please check the Error Details")
            return ""
    return text


def AI(command):
    pipe = pipeline("text-generation", model="TinyLlama/TinyLlama-1.1B-Chat-v1.0")

    prompt = (
        {"role":"system", "content":"Your name is Jarvis, an AI model inspired from movie Iron Man. Your job is to be ethical hacking assistant on Windows OS."},
        {"role":"user", "content":f"{command}"}
    )

    result = pipe(prompt)
    # Jsonify the response and extract the assistant's content
    for message in result[0]["generated_text"]:
        if message["role"] == "assistant":
            reply = message["content"]
            return reply


# Just a test. Nothing Serious
# response = AI("Who are you?")
# print(response)

if __name__ == "__main__":
    # userInput = listen().lower()
    userInput = "Who are you?"
    output = AI(userInput)
    speak(output)
    print(output)