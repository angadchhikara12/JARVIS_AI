import speech_recognition as sr

def listen():
    r = sr.Recognizer()
    with sr.Microphone() as s:
        print("Listening...")
        audio = r.listen(s)
        try:
            print("Recognizing...")
            text = r.recognize_google(audio)
            return text
        except sr.UnknownValueError:
            print("Sorry, I did not understand that.")
        except sr.RequestError:
            print("Sorry, my speech service is down.")
    return ""
