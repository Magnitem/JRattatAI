from openai import OpenAI
from RealtimeSTT import AudioToTextRecorder
import json


with open('config.json', "r") as f:
    config = json.load(f)

class AI:
    instructions="you're a kitchen assistant ready to bring up instructions any time."

    def __init__(self, openai_key: str):
        self.client = OpenAI(api_key=openai_key)

    def ask(self, inpt: str) -> str:
        return self.client.responses.create(
            model="o4-mini",
            instructions=self.instructions,
            input=inpt
        ).output_text

#voice recognition!!
class SR:
    #process_text is a function!!!
    def __init__(self, process_text):
        self.recorder = AudioToTextRecorder()

        input("start?")
        self.recorder.start()
        input("")
        self.recorder.text(process_text)

def process_text(text):
    print(f"{type(text)}: {text}")

def main():
    #ai=AI(config["openai_key"])
    SR(process_text)

if __name__ == "__main__":
    main()
