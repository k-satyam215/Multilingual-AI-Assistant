import speech_recognition as sr
import google.generativeai as genai
from dotenv import load_dotenv
import os
from gtts import gTTS

load_dotenv()
os.environ['GOOGLE_API_KEY'] = os.getenv("GOOGLE_API_KEY")
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")

def voice_input():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        audio = r.listen(source)
    try:
        text = r.recognize_google(audio)
        print('You said:', text)
        return text
    except sr.UnknownValueError:
        print('Sorry, could not understand the audio.')
        return None
    except sr.RequestError as e:
        print('could not request results from google speech recognition service; {0}'.format(e))
        return None
    

def llm_model(user_text):
    if not user_text or not str(user_text).strip():
        return "I couldn't understand your input. Please try again."

    genai.configure(api_key=GOOGLE_API_KEY)
    model = genai.GenerativeModel('gemini-2.5-flash')
    response = model.generate_content(user_text)
    return response.text         


def text_to_speech(text):
    tts = gTTS(text=text, lang='en')
    tts.save('speech.mp3')
