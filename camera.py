import cv2 #idk why this shit is not working
import speech_recognition as sr
import pyttsx3
import time
class speaker:
    def __init__(self, volume, rate, voices):
        self.volume = volume
        self.rate = rate
        self.voices = voices
    @staticmethod
    def speak(text):
        engine = pyttsx3.init()
        engine.setProperty('volume', 1.0)   #volume min 0 max 1
        engine.setProperty('rate', 120)    #rate min 1 max 150
        voices = engine.getProperty('voices')
        engine.setProperty('voice', voices[2].id) #voices 0 - java voice, 1 - Italian acent voice, 2 - just a woman
        engine.say(text)
        engine.runAndWait()
class camaeracv:    
    def cameracv(self, number=0, resolution=(1280, 720), fps=30, name="Camera"): #Camera changes
        self.number = number
        self.resolution = resolution
        self.fps = fps
        self.name = name
        self.cam = cv2.VideoCapture(self.number)
        self.cam.set(cv2.CAP_PROP_FRAME_WIDTH, self.resolutiom[0])
        self.cam.set(cv2.CAP_PROP_FRAME_HEIGHT, self.resolution[1])
        self.cam.set(cv2.CAP_PROP_FPS, self.fps)

        if not self.cam.isOpened():
            speaker.speak('There is no camera')
    def info(self):
        return f"{self.name} | number: {self.number}, jakość: {self.resolution}, fps: {self.fps}"
    def take_photo(self, filename="photo.jpg"):
        ret, frame = self.cam.read()
        if ret:
            cv2.imwrite(filename,frame)
            speaker.speak("Photo was taken")
            print("photo: {filename}")
        else:
            speaker.speak("error")
    def release(self):
        self.cam.release()
        cv2.destroyAllWindows()
cam = cameracv(number=0, resolution=(1920, 1080), fps=30, name="Camera №1") #TOTAL SHIT
cam.take_photo('photo.jpg') #take photo
cam.release()
