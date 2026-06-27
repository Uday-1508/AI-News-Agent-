from crewai import Agent, LLM
from crewai_tools import SerperDevTool
from dotenv import load_dotenv
import os

load_dotenv()
llm = LLM(
    model="gemini/gemini-2.5-flash",
    api_key=os.getenv("GEMINI_API_KEY")
)

search_tool = SerperDevTool() # tool perform tasks, here it let search google

researcher = Agent(
    role="AI Researcher",
    goal="Find accurate and latest AI news",
    backstory=(
        "You are an expert AI researcher. "
        "You always search the web before answering."
    ),
    tools=[search_tool],
    llm=llm,
    verbose=True
)