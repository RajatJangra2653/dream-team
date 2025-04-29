import semantic_kernel as sk
from semantic_kernel.connectors.ai.open_ai import AzureChatCompletion
import os

kernel = sk.Kernel()
kernel.add_text_completion_service("openai", AzureChatCompletion(
    deployment_name="gpt-35-turbo",
    endpoint=os.getenv("AZURE_OPENAI_ENDPOINT"),
    api_key=os.getenv("AZURE_OPENAI_KEY")
))