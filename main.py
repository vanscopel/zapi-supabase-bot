from supabase import create_client
import os
from dotenv import load_dotenv

#carrega variaveis env
url = os.getenv("SUPABASE_URL")
key = os.getenv("SUPABASE_KEY")

#cria conexao
supabase = create_client(url, key)

#busca dados
response = supabase.table("contatos").select("*").execute()
print(response.data)