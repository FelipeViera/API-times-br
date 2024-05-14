#É aqui que será escrito a API REST Times BR

import pandas as pd
from flask import Flask, jsonify

app = Flask(__name__)
@app.route('/')
def homepage():
    return "Teste de API RESTful"

@app.route('/d123')
def d123():

    # Ler o arquivo Excel`
    tabela = pd.read_excel('Times-br.xlsx')
    caracteres = len(tabela['Times'])
    resposta = {}
    caracteres = len(tabela['Times'])
    for c in range(0, caracteres):
        resposta.setdefault('Times', []).append(tabela['Times'][c])

    return jsonify(resposta)

app.run(host='0.0.0.0')