from google.adk.agents import Agent
from backend.utils.pdf_tool import read_pdf

root_agent = Agent(
    name="tutor_agent",
    model="gemini-2.5-flash",
    description="Explains academic concepts to students.",
    instruction="""
You are StudyBuddy AI's Tutor Agent.

Your responsibilities:
- Explain concepts step by step.
- Use simple language.
- Give practical examples.
- Encourage the student.
- End with a short recap.
""",
    tools=[read_pdf],
)