from langchain_community.chat_message_histories import SQLChatMessageHistory
from langchain_core.messages import trim_messages

# criando a memoria (historico): retorna o historico de mensagens com base no 'session_id'

def get_session_history(session_id):
    return SQLChatMessageHistory(session_id, connection="sqlite:///memory.db")

# criando a função que corta o historico e captura as 10 ultimas mensagens trocadas na conversa:
trimmeer = trim_messages(strategy="last", max_tokens=10, token_counter=len)