from langchain.memory import ConversationBufferMemory

def init_memory():
  
  memory= ConversationBufferMemory(
    memory_key='chat_history',
    return_messages=True)
  
  return memory