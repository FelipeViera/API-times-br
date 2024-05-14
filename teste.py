import requests
import json

link = "cole aqui seu link/times"
cotacoes = requests.get(link)
resposta = cotacoes.json()
print(resposta)
print(len(resposta))