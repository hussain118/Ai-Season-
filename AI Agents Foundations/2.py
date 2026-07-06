import os
import sys
from dotenv import load_dotenv
from openai import OpenAI
load_dotenv()
client=OpenAI(
      api_key=os.getenv("GEMINI_API_KEY"),
        base_url=os.getenv("base_url"),
)
def task2():
    print("=== TASK 2: Q&A Bot ===")
    print("Type 'quit' to exit.\n")
    text=input("")
    for(text!=" quit")
    response = client.chat.completions.create(
        model=os.getenv("MODEL"),
        messages=[
            {
                "role": "user",
                "content": text,
            }
        ],
    )
    Response=text.choices[0].message.content
    print("reply", response)