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

def task3():
    print("=== TASK 3: Chatbot with Memory (streaming) ===")
    print("Type 'quit' to exit.\n")
    history = [
        {"role": "system", "content": "You are a helpful assistant."}
    ]

    while True:
        user_msg = input("You: ")
        if user_msg == "quit":
            print("goodbye")
            break

        history.append({"role": "user", "content": user_msg})

        response = client.chat.completions.create(
            model=os.getenv("MODEL"),
            messages=history,
            stream=True,                     
        )

        print("Bot: ", end="", flush=True)
        jawab = ""                          
        for chunk in response:              #)
            if not chunk.choices:           
                continue
            delta = chunk.choices[0].delta.content
            if delta is None:               
                continue
            print(delta, end="", flush=True)   
            jawab += delta                 

        print("\n")                        

        history.append({"role": "assistant", "content": jawab})

task3()