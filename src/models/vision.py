import base64
import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()  # 🔥 THIS loads your .env

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))


def encode_image(image_path):
    with open(image_path, "rb") as image_file:
        return base64.b64encode(image_file.read()).decode("utf-8")


def describe_image(image_path):
    base64_image = encode_image(image_path)

    response = client.chat.completions.create(
        model="gpt-4o-mini",  # ✅ Model defined HERE
        messages=[
            {
                "role": "user",
                "content": [
                    {"type": "text", "text": "Describe this engineering image in detail."},
                    {
                        "type": "image_url",
                        "image_url": f"data:image/png;base64,{base64_image}",
                    },
                ],
            }
        ],
        max_tokens=300,
    )

    return response.choices[0].message.content