import pyttsx3
class speaker:
    def __init__(self, volume, rate, voices):
        self.volume = volume
        self.rate = rate
        self.voices = voices
    def speak(text):
        engine = pyttsx3.init()
        engine.setProperty('volume', 1.0)   #volume
        engine.setProperty('rate', 120)    #rate
        voices = engine.getProperty('voices')
        engine.setProperty('voice', voices[1].id)
        engine.say(text)
        engine.runAndWait()
speaker.speak("Hello, I'am RattatAI, for shourt RT")
speaker.speak("Today we are going to cook the pizza")