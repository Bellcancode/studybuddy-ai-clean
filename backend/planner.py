from google import genai
from dotenv import load_dotenv
import os

load_dotenv()

client = genai.Client(
    api_key=os.getenv("GEMINI_API_KEY")
)

def generate_study_plan(text):

    prompt = f"""
You are StudyBuddy AI's Study Planner.

Create a personalized 7-day study plan from the study material below.

Requirements:
- Divide the content across 7 days.
- Include realistic daily goals.
- Include short breaks.
- Include revision sessions.
- End with a final revision and self-test.
- Format the response clearly.

Study Material:

{text}
"""

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt,
    )

    return response.text