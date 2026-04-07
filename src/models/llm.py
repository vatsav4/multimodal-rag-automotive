import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

client = OpenAI(api_key=os.getenv("OPEN_API_KEY"))


def generate_answer(context, question):
    prompt = f"""
You are an expert automobile manufacturing engineer.

Answer ONLY using the provided context.
If answer is not found, say "Not found in document".

Context:
{context}

Question:
{question}

Also mention source page numbers if available.
"""

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": prompt}],
        max_tokens=300,
    )

    return response.choices[0].message.content