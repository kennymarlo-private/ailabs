from langchain.memory import ConversationBufferMemory

def create_conversation_buffer_memory(input_key, memory_key):
    conversation_buffer_memory = ConversationBufferMemory(input_key=input_key, memory_key=memory_key)
    return conversation_buffer_memory