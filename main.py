from openai import OpenAI
import json

from speech import SR
import ai

with open('config.json', "r") as f:
    config = json.load(f)

class AI:
    instructions="""you're a kitchen assistant ready to bring up instructions any time.
    The user is talking to you through a device equiped with a microphone, camera and speakers whith which you communicate with him.
    If the user requests to change the volume PREFIX the string with [vol*%] like this '[vol+5%]content of your response' (the +5% can be replaced with -5% or any integer)"""

    def __init__(self, ai_model: str, api_key: str):
        match ai_model:
            case "chatgpt-4o": self.ai=ai.chatgpt("chatgpt-4o", self.instructions, api_key)
            case _: raise Exception(f"no such ai model as {self.ai_model}")

    def ask(self, inpt: str) -> str: return self.ai.ask(inpt)

# handle the "[command]"
def handle_commands(commands: str):
    i=0
    match commands[i:(i+3)]:
            case "vol": print("TODO!!!")

def handle_text(text, args: (AI,)):
    ai=args[0]
    print(f"{type(text)}: {text}")
    #TODO
    #response = ai.ask(text)
    response: str = "[vol+5%]content"
    print(f"ai: {response}")
    
    # seperate the commands from [*]
    content=response
    if response[0]=='[': 
        i=1
        while response[i]!=']': i+=1
        handle_commands(response[1:(i-1)])
        content=response[(i+1):]

    print(f"content: {content}")
    

def main():
    ai=AI(config["ai-model"], config["api_key"])
    sr = SR()
    sr.listen(handle_text, (ai,))

if __name__ == "__main__":
    main()
