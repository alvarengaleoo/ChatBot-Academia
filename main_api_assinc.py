from chain_de_classificacao_e_roteamento import chain_de_roteamento
from chain_personal import chain_personal
from chain_atendimento_geral import chain_de_atendimento_geral
from chain_temas_nao_relacionados import chain_temas_nao_relacionados
from memoria_sistema_assincrono import get_session_history, trimmer

from operator import itemgetter
from langchain_core.runnables import RunnableLambda, RunnableParallel, RunnablePassthrough
from langchain_core.runnables.history import RunnableWithMessageHistory


## Definindo a função de escolha de roteamento
def executa_roteamento(entrada: dict):
    if entrada["resposta_pydantic"].opcao == 1:
        print(f">> Opção classe Pydantic: {entrada['resposta_pydantic'].opcao} (Atendimento Geral)")
        return RunnableLambda(lambda x: {"input_user": x['input'], "history": x['history']}) | chain_de_atendimento_geral
    elif entrada["resposta_pydantic"].opcao == 2:
        print(f">> Opção classe Pydantic: {entrada['resposta_pydantic'].opcao} (Atendimento realizado pelo personal)")
        return RunnableLambda(lambda x: {"input_user": x['input'], "history": x['history']}) | chain_personal
    else:
        print(f">> Opção classe Pydantic: {entrada['resposta_pydantic'].opcao} (Assuntos não relacionados à academia)")
        return RunnableLambda(lambda x: {"input_user": x['input'], "history": x['history']}) | chain_temas_nao_relacionados


# Cadeia final
chain_principal = (RunnableParallel({"input": itemgetter("input"),
                                     "history": itemgetter("history"),
                                     "resposta_pydantic": chain_de_roteamento
                                     })
                   | RunnableLambda(executa_roteamento))


# Chain com trimming
chain_principal_com_trimming = (
    RunnablePassthrough.assign(history=itemgetter("history") | trimmer)
    | chain_principal
)


# Definindo o runnable com histórico
runnable_with_history = RunnableWithMessageHistory(
    chain_principal_com_trimming,
    get_session_history,
    input_messages_key="input",
    history_messages_key="history",
)


