import requests
import json

link = "http://192.168.0.103:5000/d123"
cotacoes = requests.get(link)
resposta = cotacoes.json()
print(resposta)