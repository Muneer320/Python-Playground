import pyttsx3

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


with open ('lyrics.txt', "r") as l:
    speak("Your song goes like this")
    speak(l.read())
    print(l.read())

speak('lol')