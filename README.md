# Z-API + SUPABASE BOT
Projeto em Python que lê contatos do Supabase e envia mensagens via Z-API.

## 🚀 TECNOLOGIAS
-Python
-Supabase
-Z-API

## TABELA NO SUPABASE
Tabela: contatos

-id (int)
-nome(text)
-telefone (text)

## VAR (VARIAVEL DE AMBIENTE)
SUPABASE_URL=sua_supabase_url
SUPABASE_KEY=sua_supabase_key

ZAPI_INSTANCE_ID=...
ZAPI_TOKEN=...

## COMO RODAR 
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
python main.py

## RESULTADOS
Envia mensagens no formato:
"Olá, <nome_contato>! Tudo bem com você?"
Para até 3 contatos do banco.