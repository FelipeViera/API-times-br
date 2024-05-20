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
    tabela = pd.read_excel('br.xlsx')
    # Conta a quantidade de elementos
    caracteres = len(tabela['Times'])
    resposta = {}
    for c in range(0, 20):

        estaduais = int(tabela['Estaduais'][c])
        resposta.setdefault(tabela['Times'][c], []).append("Estaduais: " + str(estaduais))

        nacionais = int(tabela['Copa-br'][c]) + int(tabela['Serie-A'][c]) + int(tabela['Supercopa-br'][c])
        resposta.setdefault(tabela['Times'][c], []).append("Nacionais: " + str(nacionais))

        continentais = int(tabela['Libertadores'][c]) + int(tabela['Sul-americana'][c]) + int(tabela['Recopa'][c])
        resposta.setdefault(tabela['Times'][c], []).append("Continentais: " + str(continentais))

        total = continentais + nacionais + estaduais
        resposta.setdefault(tabela['Times'][c], []).append("Total: " + str(total))
    return jsonify(resposta)

@app.route('/times/estaduais')
def estaduais():
    # Ler o arquivo Excel`
    tabela = pd.read_excel('br.xlsx')
    # Conta a quantidade de elementos
    caracteres = len(tabela['Times'])
    resposta = {}
    for c in range(0, 20):
        resposta.setdefault(tabela['Times'][c], []).append(str(tabela['Estaduais'][c]))

    return jsonify(resposta)

@app.route('/times/nacionais')
def nacionais():
    # Ler o arquivo Excel`
    tabela = pd.read_excel('br.xlsx')
    # Conta a quantidade de elementos
    caracteres = len(tabela['Times'])
    lista = []
    resposta = {}
    for c in range(0, 20):
        copa = int(tabela['Copa-br'][c])
        campeonato = int(tabela['Serie-A'][c])
        supercopa = int(tabela['Supercopa-br'][c])
        total = supercopa + copa + campeonato
        resposta.setdefault(tabela['Times'][c], []).append("Brasileirão: " + str(campeonato))
        resposta.setdefault(tabela['Times'][c], []).append("Copa do Brasil: " + str(copa))
        resposta.setdefault(tabela['Times'][c], []).append("Supercopa do Brasil: " + str(supercopa))
        resposta.setdefault(tabela['Times'][c], []).append("Total: " + str(total))
    return jsonify(resposta)

@app.route('/times/continentais')
def continentais():
    # Ler o arquivo Excel`
    tabela = pd.read_excel('br.xlsx')
    # Conta a quantidade de elementos
    caracteres = len(tabela['Times'])
    resposta = {}
    for c in range(0, 20):
        libertadores = int(tabela['Libertadores'][c])
        sula = int(tabela['Sul-americana'][c])
        recopa = int(tabela['Recopa'][c])
        total = sula + recopa + libertadores
        resposta.setdefault(tabela['Times'][c], []).append("Libertadores: " + str(libertadores))
        resposta.setdefault(tabela['Times'][c], []).append("Sul-americana: " + str(sula))
        resposta.setdefault(tabela['Times'][c], []).append("Recopa: " + str(recopa))
        resposta.setdefault(tabela['Times'][c], []).append("Continentais: " + str(total))
    return jsonify(resposta)

@app.route('/times/total')
def total():
    # Ler o arquivo Excel`
    tabela = pd.read_excel('br.xlsx')
    # Conta a quantidade de elementos
    caracteres = len(tabela['Times'])
    resposta = {}

    for c in range(0, 20):
        libertadores = int(tabela['Libertadores'][c])
        sula = int(tabela['Sul-americana'][c])
        recopa = int(tabela['Recopa'][c])
        continentais = sula + recopa + libertadores

        estaduais = int(tabela['Estaduais'][c])
        resposta.setdefault(tabela['Times'][c], []).append("Estaduais: "+ str(estaduais))

        copa = int(tabela['Copa-br'][c])
        campeonato = int(tabela['Serie-A'][c])
        supercopa = int(tabela['Supercopa-br'][c])
        nacionais = supercopa + copa + campeonato

        resposta.setdefault(tabela['Times'][c], []).append("Brasileirão: " + str(campeonato))
        resposta.setdefault(tabela['Times'][c], []).append("Copa do Brasil: " + str(copa))
        resposta.setdefault(tabela['Times'][c], []).append("Supercopa do Brasil: " + str(supercopa))


        resposta.setdefault(tabela['Times'][c], []).append("Libertadores: " + str(libertadores))
        resposta.setdefault(tabela['Times'][c], []).append("Sul-americana: " + str(sula))
        resposta.setdefault(tabela['Times'][c], []).append("Recopa: " + str(recopa))

        resposta.setdefault(tabela['Times'][c], []).append("Nacionais: " + str(nacionais))
        resposta.setdefault(tabela['Times'][c], []).append("Continentais: " + str(continentais))

        total = estaduais + nacionais + continentais

        resposta.setdefault(tabela['Times'][c], []).append("Total: " + str(total))

    return jsonify(resposta)

app.run(host='0.0.0.0')