from openai import OpenAI
import json
import speech_recognition as sr
import pyttsx3
import cv2
import os
import base64
photo = r#path to photo
with open('config.json', "r") as f:
    config = json.load(f)
vol = 1.0
class camera:
    def __init__(self, number=0, resolution=(1280, 720), fps=30, name="Camera"): #Camera changes
        self.number = number
        self.resolution = resolution
        self.fps = fps
        self.name = name
        self.cam = cv2.VideoCapture(self.number)
        self.cam.set(cv2.CAP_PROP_FRAME_WIDTH, self.resolution[0])
        self.cam.set(cv2.CAP_PROP_FRAME_HEIGHT, self.resolution[1])
        self.cam.set(cv2.CAP_PROP_FPS, self.fps)
        if not self.cam.isOpened():
            speaker.speak('There is no camera')
    def info(self):
        return f"{self.name} | number: {self.number}, quality: {self.resolution}, fps: {self.fps}"
    def take_photo(self, file="photo.jpg"):
        ret, frame = self.cam.read()
        if ret:
            cv2.imwrite(file,frame)
            speaker.speak("Photo was taken")
            print(f"photo: {file}")
            os.startfile(file)
            with open(file, "rb") as img_file:
                img_data = base64.b64encode(img_file.read()).decode('utf-8')
            return img_data
        else:
            speaker.speak("error")
            return None
    def release(self):
        self.cam.release()


class speaker:
    global engine
    engine = pyttsx3.init()
    def __init__(self, volume, rate, voices):
        self.volume = volume
        self.rate = rate
        self.voices = voices
    def speak(text):
        engine.setProperty('volume', vol)   #volume min 0 max 1
        engine.setProperty('rate', 120)    #rate min 1 max 150
        voices = engine.getProperty('voices')
        engine.setProperty('voice', voices[1].id) #voices 0 - java voice, 1 - Italian acent voice, 2 - just a woman
        engine.say(text)
        engine.runAndWait()

class SR:
    def listen():
        listener = sr.Recognizer()
        print("ready to work")
        
        with sr.Microphone() as micro:
            listener.pause_threshold = 1
            input_speech = listener.listen(micro)
        try:
            print("Say something")
            global query
            query = listener.recognize_google(input_speech, language="pl-PL").lower()
            print("You said:",query)
            query = input("text something:")
        except Exception as exception:
            print("I don't understand")
            print(exception)
        return query

class AI:
    instructions="""you're a kitchen assistant ready to bring up instructions any time.
    The user is talking to you through a device equiped with a microphone, camera and speakers whith which you communicate with him."""
    global client
    client = OpenAI(api_key=config["openai_key"])

    def ask(query):
        file = client.files.create(
            file=open("photo.jpg", "rb"),
            purpose="user_data"
        )

        response = client.responses.create(
            model="gpt-5",
            input=[
                {
                    "role": "user",
                    "content": [
                        {
                            "type": "input_file",
                            "file_id": file.id,
                        },
                        {
                            "type": "input_text",
                            "text": query,
                        },
                    ]
                }
            ]
        )

def main():
    global vol
    cam = camera()
    ai = AI()
    while True:
        text = SR.listen()
        if not text:
            continue
        query = text.lower().split()
        if not query:
            continue
        if len(query)>= 2 and query[0] == "hej" and query [1] == "buddie":
            query = " ".join(query[2:])
            cam.take_photo()
            ai.ask(text)

        elif query[0] == "głośniej":
            if vol<1.0:
                vol += 0.05
            else:
                speaker.speak("Kurde gdzie głośniej")
        elif query[0] == "ciszej":
            if vol>0.0:
                vol -= 0.05
            else:
                speaker.speak("Nie da się głośniej")

if __name__ == "__main__":
        main()