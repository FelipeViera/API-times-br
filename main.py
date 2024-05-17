#É aqui que será escrito a API REST Times BR

import pandas as pd
from flask import Flask, jsonify

app = Flask(__name__)
@app.route('/')
def homepage():
    return "Esta é API REST da Série A do Brasileirão."

@app.route('/times')
def times():

    # Ler o arquivo Excel`
    tabela = pd.read_excel('Times-br.xlsx')
    # Conta a quantidade de elementos
    caracteres = len(tabela['Times'])
    resposta = {}
    for c in range(0, 20):
        resposta.setdefault(tabela['Times'][c], []).append("Estaduais: " + str(tabela['estaduais'][c]))
        resposta.setdefault(tabela['Times'][c], []).append("Nacionais: " + str(tabela['nacionais'][c]))
        resposta.setdefault(tabela['Times'][c], []).append("Continentais: " + str(tabela['continentais'][c]))
        resposta.setdefault(tabela['Times'][c], []).append("Total: " + str(tabela['Total'][c]))
    return jsonify(resposta)

@app.route('/times/estaduais')
def estaduais():
    # Ler o arquivo Excel`
    tabela = pd.read_excel('Times-br.xlsx')
    # Conta a quantidade de elementos
    caracteres = len(tabela['Times'])
    lista = []
    resposta = {}
    for c in range(0, 20):
        resposta.setdefault(tabela['Times'][c], []).append(str(tabela['estaduais'][c]))
        lista.append(tabela['estaduais'][c])
    return jsonify(resposta)

@app.route('/times/nacionais')
def nacionais():
    # Ler o arquivo Excel`
    tabela = pd.read_excel('Times-br.xlsx')
    # Conta a quantidade de elementos
    caracteres = len(tabela['Times'])
    lista = []
    resposta = {}
    for c in range(0, 20):
        resposta.setdefault(tabela['Times'][c], []).append(str(tabela['nacionais'][c]))
        lista.append(tabela['nacionais'][c])
    return jsonify(resposta)

@app.route('/times/continentais')
def continentais():
    # Ler o arquivo Excel`
    tabela = pd.read_excel('Times-br.xlsx')
    # Conta a quantidade de elementos
    caracteres = len(tabela['Times'])
    lista = []
    resposta = {}
    for c in range(0, 20):
        resposta.setdefault(tabela['Times'][c], []).append(str(tabela['continentais'][c]))
        lista.append(tabela['continentais'][c])
    return jsonify(resposta)


app.run(host='0.0.0.0')