#Exceções

from typing import Text


lista = [1, 10]
arquivo = open('aula10.py', 'r')

try:
    texto = arquivo.read()
    divisao = 10 / 1
    numero = lista[1]
    x = a
except ZeroDivisionError: #Observar regra de pais e filhos no Python
    print('Não é possível realizar uma divisão por zero.')
except IndexError:
    print('Erro ao acessar um índice inválido da lista.')
except BaseException as ex:
    print('Erro desconhecido. Erro: {}'.format(ex))
else:
    print('Executa quando não ocorre exceção.')
finally:
    print('Sempre executa')
    print('Fechando arquivo')
    arquivo.close()
