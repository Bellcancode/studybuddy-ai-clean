from google.adk.agents import Agent

root_agent = Agent(
    name="summary_agent",
    model="gemini-2.5-flash",
    description="Summarizes notes, articles, and study materials.",
    instruction="""
You are StudyBuddy AI's Summary Agent.

Your job is to:
- Summarize long notes into concise points.
- Highlight the most important concepts.
- Preserve key definitions and facts.
- Use bullet points whenever appropriate.
- End with a short takeaway.
"""
)