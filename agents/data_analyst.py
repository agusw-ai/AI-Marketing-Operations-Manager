from google.adk.agents import Agent

data_analyst = Agent(
    name="data_analyst",
    model="gemini-2.5-flash",
    description="Analyze advertising datasets.",
    instruction="""
You are a Data Analyst specializing in digital advertising.

Responsibilities:
- Read advertising datasets.
- Validate data quality.
- Calculate CTR, CPC, CPM, CPA, ROAS.
- Detect trends and anomalies.
- Return structured summaries.
"""
)