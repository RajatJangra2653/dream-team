import autogen
from meeting_summary_agent import summary_agent
from task_management_agent import task_agent

group_chat = autogen.GroupChat(agents=[summary_agent, task_agent], messages=[])
manager = autogen.GroupChatManager()
manager.manage(group_chat)