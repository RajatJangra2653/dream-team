import os
import autogen

summary_agent = autogen.AssistantAgent("MeetingSummaryAgent", llm_config={
    "api_key": os.getenv('AZURE_OPENAI_KEY'),
    "endpoint": os.getenv('AZURE_OPENAI_ENDPOINT')
})