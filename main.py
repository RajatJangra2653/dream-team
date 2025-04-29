import autogen
from meeting_summary_agent import summary_agent
from task_management_agent import task_agent

user_proxy = autogen.UserProxyAgent("team_member", human_input_mode="TERMINATE", llm_config={})
user_proxy.initiate_chat(summary_agent, message="Provide today's meeting summary.")