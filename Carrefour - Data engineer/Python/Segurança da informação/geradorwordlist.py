import itertools

string = input('Digite a palvra a ser permutada: ')

resultado = itertools.permutations(string, len(string))

contagem = 0

for i in resultado:
    print(''.join(i))
    contagem += 1

print(f'Permutações possíveis: {contagem}')