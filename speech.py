import speech_recognition as sr

class SR:
    def listen()
        listener = sr.Recognizer()
        print("Gotów do słuchania")
        
        with sr.Microphone() as micro:
            listener.pause_treshhold = 1
            input_speech = listener.listen(micro)
        try
            print("Czekam na komendy")
            query = listener.recognise_google(input_speech, language="pl-Pl")
            print("Youn said:",query)
        except:
            print("I don't understand")
            print(exception)
