import os
import autogen

task_agent = autogen.AssistantAgent("TaskManagementAgent", llm_config={
    "api_key": os.getenv('AZURE_OPENAI_KEY'),
    "endpoint": os.getenv('AZURE_OPENAI_ENDPOINT')
})