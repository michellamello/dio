import re, json
from urllib.request import urlopen

url = 'https://ipinfo.io/json'

resposta = urlopen(url)

dados = json.load(resposta)

ip = dados['ip']
org = dados['org']
cidade = dados['city']
pais = dados['country']
regiao = dados['region']

print('Detalhes do IP externo\n')
print(f'{ip} {org} {cidade} {pais} {regiao}')