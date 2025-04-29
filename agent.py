import os
from openai import AzureOpenAI

def assist_meeting(prompt):
    client = AzureOpenAI(api_key=os.getenv('AZURE_OPENAI_KEY'), endpoint=os.getenv('AZURE_OPENAI_ENDPOINT'))
    response = client.ChatCompletion.create(model="gpt-35-turbo", messages=[{"role": "user", "content": prompt}])
    return response['choices'][0]['message']['content']

print(assist_meeting("Summarize today's meeting discussion."))