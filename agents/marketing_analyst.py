from google.adk.agents import Agent

marketing_analyst = Agent(
    name="marketing_analyst",
    model="gemini-2.5-flash",
    description="Analyze marketing campaign performance.",
    instruction="""
    You are an expert Digital Marketing Analyst.

    Analyze marketing metrics such as:
    - ROAS
    - CTR
    - CPC
    - CPA
    - Conversion Rate

    Provide concise and actionable business recommendations.
    """
)