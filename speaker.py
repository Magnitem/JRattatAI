import pyttsx3
def speak(text):
    engine = pyttsx3.init()
    engine.setProperty('volume', 1.0)   #volume
    engine.setProperty('rate', 150)    #rate
    engine.setProperty('voice', voices[1].id)
    engine.say(text)
    engine.runAndWait()
    