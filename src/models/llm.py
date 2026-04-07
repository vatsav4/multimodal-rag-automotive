from transformers import pipeline

# Load lightweight model
generator = pipeline("text-generation", model="distilgpt2")


def generate_answer(context, question):
    prompt = f"""
Context:
{context}

Question:
{question}

Answer:
"""

    result = generator(prompt, max_length=200, num_return_sequences=1)

    return result[0]["generated_text"]