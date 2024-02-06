import requests
import re
import xml.etree.ElementTree as ET

"""
Pegando o codigo iso e o nome das moedas de cada pais que a API disponibiliza.
E tambem pegando todas as combinacoes possivel que a APi permite.
Esses dados estao disponiveis em xml, nos nomes das moedas é simplesmete extrair o conteudo da requisição
com a biblioteca xml importada e iterar sob o objeto gerado, adicionando cada nome em uma lista.
Na parte do codigo da moeda elas estavão em tags Ex.:<EUR>EURO<\EUR> então usei o regex para pegar somente a sequência
de caracteres que estão entre os caracteres especias <> e que não começam com \.
"""


Req = requests.get('https://economia.awesomeapi.com.br/xml/available/uniq')
combinacoes = requests.get('https://economia.awesomeapi.com.br/xml/available').text
nome = Req.content
moeda = Req.text
root = ET.fromstring(nome)
nomes = [i.text for i in root]

t = re.compile(r'\<[^/].{0,6}\>')
t_combinacao = re.compile(r'\<[^/].{0,9}\>')
check_combinacao = re.findall(t_combinacao, combinacoes)
check = re.findall(t, moeda)


combinacoes_moedas = []
for i in check_combinacao:
    combinacoes_moedas.append(i.replace("<", "").replace(">", ""))
combinacoes_moedas.remove('xml')


moedas = []
for c in check:
    moedas.append(c.replace("<", "").replace(">", ""))
moedas.remove('xml') #removendo a tag inicial <xml>
moedas.insert(97, 'NGNPARALLEL')#inserindo o unico codigo que nao tinha passado pelo compilador

#print(nomes.count('Dólar Americano'))
for moeda in moedas:
    #dois nomes iguais com valores diferentes sendo que USDT não esta dentro das combinações possiveis determinadas na API
    if moeda == "USDT":
        moedas[moedas.index(moeda)] = moeda.replace("USDT", "USD")


moeda_dicionario = {}

for i in range(len(nomes)):
    moeda_dicionario[nomes[i]] = moedas[i]

