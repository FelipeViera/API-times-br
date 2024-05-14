import pandas as pd
tabela = pd.read_excel('Times-br.xlsx')
#Conta a quantidade de elementos
resposta = {}
caracteres = len(tabela['Times'])
for c in range(0, caracteres):
    resposta.setdefault(tabela['Times'][c], []).append("Estaduais: " + str(tabela['estaduais'][c]))
    resposta.setdefault(tabela['Times'][c], []).append("Nacionais: " + str(tabela['nacionais'][c]))
    resposta.setdefault(tabela['Times'][c], []).append("Continentais: " + str(tabela['continentais'][c]))
    resposta.setdefault(tabela['Times'][c], []).append("Total: " + str(tabela['Total'][c]))
print(resposta)