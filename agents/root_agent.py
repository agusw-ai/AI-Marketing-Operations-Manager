from google.adk.agents import Agent
from agents.marketing_analyst import marketing_analyst
from agents.data_analyst import data_analyst
from agents.business_consultant import business_consultant

root_agent = Agent(
    name="marketing_operations_manager",
    model="gemini-2.5-flash",
    description="AI Marketing Operations Manager",
    instruction="""
You are an AI Marketing Operations Manager.

Responsibilities:
- Analyze marketing campaign performance.
- Provide business recommendations.
- Coordinate specialized agents.
- Generate executive summaries.
"""
)