import os
import sys
from dotenv import load_dotenv
from openai import OpenAI
sys.stdout.reconfigure(encoding="utf-8")

load_dotenv()
client= OpenAI(
   
    api_key=os.getenv("GEMINI_API_KEY"),
    base_url=os.getenv("base_url")
    )
def task3():
    print("=== TASK 3: Chatbot with Memory ===")
    print("Type 'quit' to exit.\n")
    history = [
        {"role": "system", "content": "You are a helpful assistant."}
    ]

    while True:
        user_msg=input("you")
        if user_msg=="quit":
            print("goodbye")
            break
    history.append({
        "role": "user",
        "content": user_msg
    }
        
    )
    response=  client.chat.completion.create(
            model=os.getenv("MODEL")
            messages=history
        )
    
    jawab=response.choices[0].content
    history.append(
        {
            "role": "assitant",
             "content": jawab
            
        }
    )
    