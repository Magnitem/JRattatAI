import speech_recognition as sr

class SR:
    def __init__(self):
        self.r   = sr.Recognizer()
        self.mic = sr.Microphone()
        
        with self.mic as source: self.r.adjust_for_ambient_noise(source)
    # handler is a function taking string
    def listen(self, handler, handler_args):
        with self.mic as source:

            while True:
                print("listening!")
                audio = self.r.listen(self.mic)
                print("listened")
                try:
                    text = self.r.recognize_whisper(audio)
                    handler(text, handler_args)
                except sr.UnknownValueError:
                    handler("cannot understand", handler_args)
                except sr.RequestError as e:
                    print("API UNAVAILABLE: ", e)
                    handler("API unavailable: ", e)
