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



PROMPT = "Write a one-sentence motivational quote"

print("=== temperature: 0.0 (focused) ===")
cold = client.chat.completions.create(
    model=os.getenv("MODEL"),
    messages=[{"role": "user", "content": PROMPT}],
    temperature=0.0,
)
print(cold.choices[0].message.content)




print("\n=== temperature: 0.7 (creative) ===")
hot = client.chat.completions.create(
    model=os.getenv("MODEL"),
    messages=[{"role": "user", "content": PROMPT}],
    temperature=0.7,
)
print(hot.choices[0].message.content)
