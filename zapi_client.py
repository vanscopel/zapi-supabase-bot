import requests
import os

INSTANCE_ID = os.getenv("ZAPI_INSTANCE_ID")
TOKEN = os.getenv("ZAPI_TOKEN")
CLIENT_TOKEN = os.getenv("ZAPI_CLIENT_TOKEN")

URL = f"https://api.z-api.io/instances/{INSTANCE_ID}/token/{TOKEN}/send-text"

def enviar_mensagem(telefone, mensagem):
    payload = {
        "phone": telefone,
        "message": mensagem
    }
    headers = {
        "Client-Token": CLIENT_TOKEN
    }

    response = requests.post(URL, json=payload, headers=headers)
    return response.status_code, response.text