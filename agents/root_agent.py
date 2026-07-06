from google.adk.agents import Agent

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