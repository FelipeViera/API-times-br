import pandas as pd
tabela = pd.read_excel('Times-br.xlsx')
#Conta a quantidade de elementos
resposta = {}
caracteres = len(tabela['Times'])
for c in range(0, caracteres):
    resposta.setdefault('Times', []).append(tabela['Times'][c])
print(resposta['Times'])