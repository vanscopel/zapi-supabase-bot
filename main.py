from supabase import create_client
from dotenv import load_dotenv
import os
import requests


#carregar .env
load_dotenv()

#supabase
url = os.getenv("SUPABASE_URL")
key = os.getenv("SUPABASE_KEY")
supabase = create_client(url, key)

#z-api
INSTANCE_ID = os.getenv("ZAPI_INSTANCE_ID")
TOKEN = os.getenv("ZAPI_TOKEN")
ZAPI_URL = f"https://api.z-api.io/instances/{INSTANCE_ID}/send-text"

headers= {
    "Client-Token": os.getenv("ZAPI_CLIENT_TOKEN")
}

#buscar contatos 
contatos= supabase.table("contatos").select("*").limit(3).execute().data

if not contatos:
    print("Nenhum contato encontrado.")
    exit()

#enviar mensagem
for contato in contatos:
    nome = contato.get("nome")
    telefone = contato.get("telefone")
    mensagem= f"Olá, {nome}! Tudo bem com você?"

    payload= {
        "phone": telefone,
        "message": mensagem
    }

    response= requests.post(ZAPI_URL, json=payload, headers=headers)

    if response.status_code == 200:
        print(f"[SUCESSO] {nome}")
    else:
        print(f"[ERRO] {nome} -> {response.text}")