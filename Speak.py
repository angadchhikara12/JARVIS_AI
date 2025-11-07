from elevenlabs.play import play # Imported `play` function form ElevenLabs package
from elevenlabs.client import ElevenLabs # Imported ElevenLabs Client
from dotenv import load_dotenv # Imported .env file loader to import secret keys/APIs
import os # Imported os to access environment variables

load_dotenv() # Loading .env file
client = ElevenLabs( # Initializing ElevenLabs Client with API key
    api_key = os.getenv("ELEVENLABS_API_KEY") # Accessing ElevenLabs API key from environment variables
)

# Function to convert text to speech and play it
def speak(text):
    audio = client.text_to_speech.convert(voice_id="5hZv9mAOcmcMt1TxA5Iz", text=text, model_id="eleven_multilingual_v2", output_format="mp3_44100_128")
    play(audio)

speak("System Engaging.")