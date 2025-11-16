from openai import OpenAI
import json

from speech import SR

with open('config.json', "r") as f:
    config = json.load(f)

class AI:
    instructions="""you're a kitchen assistant ready to bring up instructions any time.
    The user is talking to you through a device equiped with a microphone, camera and speakers whith which you communicate with him.
    If the user requests to change the volume PREFIX the string with [vol*%] like this '[vol+5%]content of your response' (the +5% can be replaced with -5% or any integer)"""

    def __init__(self, openai_key: str):
        self.client = OpenAI(api_key=openai_key)

    def ask(self, inpt: str) -> str:
        return self.client.responses.create(
            model="o4-mini",
            instructions=self.instructions,
            input=inpt
        ).output_text

# handle the "[command]"
def handle_commands(commands: str):
    i=0
    match commands[i:(i+3)]:
            case "vol": print("TODO!!!")

def handle_text(text, args: (AI,)):
    ai=args[0]
    print(f"{type(text)}: {text}")
    #response = ai.ask(text)
    response = "[vol+5%]content"
    print(f"ai: {response}")
    
    content=response
    if response[0]=='[': 
        i=1
        while response[i]!=']': i+=1
        handle_commands(response[1:(i-1)])
        content=response[(i+1):]

    print(f"content: {content}")
    

def main():
    ai=AI(config["openai_key"])
    sr = SR()
    sr.listen(handle_text, (ai,))

if __name__ == "__main__":
    main()
