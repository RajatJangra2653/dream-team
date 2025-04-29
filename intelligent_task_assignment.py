from autogen import AssistantAgent
import os

task_assignment_agent = AssistantAgent("TaskAssignmentAgent", llm_config={
    "api_key": os.getenv("AZURE_OPENAI_KEY"),
    "endpoint": os.getenv("AZURE_OPENAI_ENDPOINT")
})