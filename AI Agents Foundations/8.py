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


def task8():
    print("=== TASK 8: Token Counter ===")
    questions = [
        "Hi.",
        "Explain what Python is in 2 sentences.",
        "Write a detailed explanation of how the internet works, including DNS, TCP/IP, HTTP, and servers.",
    ]

    for q in questions:                        # for (auto& q : questions)
        response = client.chat.completions.create(
            model=os.getenv("MODEL"),
            messages=[{"role": "user", "content": q}]   # fresh, no history needed
        )

        usage = response.usage                 # token stats live here

        print(f"\nQuestion: {q}")
        print(f"  prompt_tokens:     {usage.prompt_tokens}")      # what YOU sent
        print(f"  completion_tokens: {usage.completion_tokens}")  # what the MODEL wrote
        print(f"  total_tokens:      {usage.total_tokens}")       # sum of both