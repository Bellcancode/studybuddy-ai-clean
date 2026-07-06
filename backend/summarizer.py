from google import genai
from dotenv import load_dotenv
import os

load_dotenv()

client = genai.Client(
    api_key=os.getenv("GEMINI_API_KEY")
)

def summarize_text(text):

    prompt = f"""
You are StudyBuddy AI.

Summarize the following study material.

Requirements:
- Use simple language.
- Keep important points.
- Use bullet points.
- Maximum 300 words.

Study Material:

{text}
"""

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt,
    )

    return response.text