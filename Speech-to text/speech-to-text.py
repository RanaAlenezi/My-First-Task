from gtts import gTTS
import speech_recognition as sr

r = sr.Recognizer()
with sr.Microphone() as src:
    print('Say something....')
    audio = r.listen(src)
try:
    t = r.recognize_google(audio, language='ar-AR')
    print(t)
except sr.UnknownValueError as U:
    print(U)
except sr.RequestError as R:
    print(R)
