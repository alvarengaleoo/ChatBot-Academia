from langchain_community.chat_message_histories import SQLChatMessageHistory
from langchain_core.messages import trim_messages
from sqlalchemy.ext.asyncio import create_async_engine

# Engine ASSÍNCRONA (compatível com FastAPI/LangServe)
async_engine = create_async_engine("sqlite+aiosqlite:///memory.db")

def get_session_history(session_id):
    return SQLChatMessageHistory(session_id, connection=async_engine, async_mode=True)

# Criando a função que corta o histórico e captura as 10 ultimas mensagens trocadas na conversa:
trimmer = trim_messages(strategy="last", max_tokens=10, token_counter=len)