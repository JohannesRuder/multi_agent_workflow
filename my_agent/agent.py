from pathlib import Path

from google.adk.agents.llm_agent import Agent

try:
    from dotenv import load_dotenv

    load_dotenv(Path(__file__).resolve().parents[1] / ".env")
except Exception:
    pass

root_agent = Agent(
    model="gemini-2.5-flash",
    name="root_agent",
    description="A helpful assistant for user questions.",
    instruction="Answer user questions to the best of your knowledge",
)
