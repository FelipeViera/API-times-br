import requests
import json

link = "cole aqui seu link host/times"
cotacoes = requests.get(link)
resposta = cotacoes.json()
print(resposta)