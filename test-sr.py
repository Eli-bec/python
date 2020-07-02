import speech_recognition as sr

r = sr.Recognizer()

mic = sr.Microphone()

with mic as src:
    r.adjust_for_ambient_noise(src)
    audio = r.listen(src)

print(r.recognize_google(audio))
