import os
import sys
from dotenv import load_dotenv
from openai import OpenAI
sys.stdout.reconfigure(encoding="utf-8")

load_dotenv()
client= OpenAI(
   
    api_key=os.getenv("GEMINI_API_KEY"),
        base_url=os.getenv("base_url"),
)


Ans=client.chat.completions.create(
    model=os.getenv("MODEL"),
    messages=[
        {
        "role":"user",
        "content":"Do you add your opinion in ans"
        }
        ],
    )
Text=Ans.choices[0].message.content
print("Reply", Text)