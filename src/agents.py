from langchain.agents import AgentType,initialize_agent
from langchain.chat_models import init_chat_model
from tools import init_tools
from dotenv import load_dotenv

load_dotenv()


def init_agent(memory):

  model=init_chat_model('gpt-4.1-nano',model_provider='openai')
  tools=init_tools()

  agent=initialize_agent(
    llm=model,
    tools=tools,
    agent=AgentType.CHAT_CONVERSATIONAL_REACT_DESCRIPTION,
    memory=memory,
    temperature=0.8,
    verbose=True,)
  
  return agent