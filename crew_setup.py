from crewai import Crew, Process
from agents import researcher
from tasks import research_task

crew = Crew(
    agents=[researcher],
    tasks=[research_task],
    process=Process.sequential,
    verbose=True
)