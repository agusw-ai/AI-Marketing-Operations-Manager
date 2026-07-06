from google.adk.agents import Agent
from agents.marketing_analyst import marketing_analyst
from agents.data_analyst import data_analyst
from agents.business_consultant import business_consultant

root_agent = Agent(
    name="marketing_operations_manager",

    model="gemini-2.5-flash",

    description="AI Marketing Operations Manager",

    instruction="""
You are the coordinator of an AI Marketing Operations Manager.

Delegate tasks to the appropriate specialist.

Available specialists:

- Data Analyst
- Marketing Analyst
- Business Consultant

When answering users:

1. Decide which specialist should handle the task.
2. Use the specialist's expertise.
3. Produce one clear final answer.
""",

    sub_agents=[
        data_analyst,
        marketing_analyst,
        business_consultant,
    ],
)