from crewai import Task
from agents import researcher

research_task = Task(
    description="""
    Search the internet for the most important AI news published today or in the last 24 hours.

    Find the top 10 biggest AI stories from anywhere in the world.

    Do NOT focus on specific companies.
    Include only news that is actually important and recent.

    For each news item provide:
    1. Headline
    2. Company/Organization (if applicable)
    3. What happened
    4. Why it matters
    5. Source link
    """,
    expected_output="""
    A well-formatted report of the top 10 latest AI news stories from around the world.
    """,
    agent=researcher
)