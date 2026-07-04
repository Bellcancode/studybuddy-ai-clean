from google.adk.agents import Agent

from .tutor import root_agent as tutor_agent
from .quiz import root_agent as quiz_agent
from .summery import root_agent as summary_agent
from .planner import root_agent as planner_agent

root_agent = Agent(
    name="studybuddy_coordinator",
    model="gemini-2.5-flash",
    description="Routes user requests to the correct StudyBuddy AI specialist agent.",
    instruction="""
You are the coordinator for StudyBuddy AI.

Never answer the user's question yourself.

Instead, determine which specialist agent should handle the request.

Delegate to:

- Tutor Agent → explaining concepts.
- Quiz Agent → generating quizzes.
- Summary Agent → summarizing notes.
- Planner Agent → creating study schedules.

If a request needs multiple tasks, delegate to the appropriate agents.
""",
    sub_agents=[
        tutor_agent,
        quiz_agent,
        summary_agent,
        planner_agent,
    ],
)