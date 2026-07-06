from google import genai
from dotenv import load_dotenv
import os

load_dotenv()

client = genai.Client(
    api_key=os.getenv("GEMINI_API_KEY")
)

def generate_quiz(text):

    prompt = f"""
You are StudyBuddy AI.

Create a quiz from the study material below.

Requirements:
- Generate exactly 10 multiple-choice questions.
- Each question must have 4 options (A, B, C, D).
- Clearly indicate the correct answer.
- Cover different parts of the material.

Study Material:

{text}
"""

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt,
    )

    return response.text