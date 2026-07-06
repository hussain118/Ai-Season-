import os
import sys
from dotenv import load_dotenv
from openai import OpenAI

sys.stdout.reconfigure(encoding="utf-8")
load_dotenv()
client = OpenAI(
    api_key=os.getenv("GEMINI_API_KEY"),
    base_url=os.getenv("base_url"),
)


def task5():
    print("=== Translator ===")
    Translator=input("enter which lang you want to tranlate complete like english translator")
    history = [{"role": "system", "content": Translator}]
    
    while True:
        user_input = input("translate: ")
        if user_input == "quit":                
            print("goodbye")
            break
        history.append({
            "role": "user",
            "content": user_input
        })
        text=client.chat.completions.create(
        model=os.getenv("MODEL"),
        messages=history
    )
        word=text.choices[0].message.content
        print("Bot:", word, "\n")

        history.append({                        
            "role": "assistant",
            "content": word
        })
task5()