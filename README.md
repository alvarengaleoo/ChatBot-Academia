# Chatbot de Atendimento para Academia

## Sobre o projeto
Este projeto tem como objetivo criar um chatbot de atendimento para academia utilizando LangChain e Groq. O sistema consegue interpretar perguntas do usuário e direcionar a resposta para o fluxo adequado, como atendimento geral, dúvidas sobre treino e assuntos fora do contexto da academia.

## Tecnologias utilizadas
- Python
- LangChain
- Groq
- FastAPI
- SQLite
- python-dotenv

## Estrutura do projeto
```bash
projeto/
├── main.py
├── minha_api.py
├── chains/
├── memoria/
└── .env
```

## Instalação

Clone o repositório:

```bash
git clone URL_DO_REPOSITORIO
```

Entre na pasta:

```bash
cd nome-do-projeto
```

Crie o ambiente virtual:

```bash
python -m venv venv
```

Ative:

Windows:

```bash
venv\Scripts\activate
```

Instale as dependências:

```bash
pip install -r requirements.txt
```

## Configuração

Crie um arquivo `.env`:

```env
GROQ_API_KEY=sua_chave
```

## Executando

Rodar pelo terminal:

```bash
python main.py
```

Rodar API:

```bash
python minha_api.py
```

## Funcionalidades
- Atendimento geral da academia
- Respostas sobre treino
- Roteamento de perguntas
- Memória de conversa
- API local

## Observações
O projeto foi desenvolvido para fins de estudo e demonstração do uso de LangChain com múltiplos fluxos de atendimento.