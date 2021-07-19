#Listas e tuplas

#Listas
lista = [1, 10, 7, 5, 12]
lista_animal = ['cachorro', 'gato', 'elefante', 'lobo', 'arara']

#Multiplicando lista
nova_lista = lista_animal * 3

print(nova_lista)

#Percorrendo lista

for x in lista_animal:
    print(x)

soma = 0
for x in lista:
    print(x)
    soma += x
print(soma)

#Soma
print(sum(lista))

#Maior
print(max(lista))
print(max(lista_animal)) #Gato, pois começa com G

#Menor
print(min(lista))
print(min(lista_animal)) #Cachorro, pois começa com C

#Ordenação de lista - Menor para o maior
lista.sort()
lista_animal.sort()

print(lista)
print(lista_animal)

#Ordenação de lista - Maior para o menor
lista.reverse()
lista_animal.reverse()

print(lista)
print(lista_animal)

#In/ Append
if 'lobo' in lista_animal:
    print('Existe um lobo na lista')
else:
    print('Não existe um lobo na lista, será incluído')
    lista_animal.append('lobo')
    print(lista_animal)

#Pop - Retira último item da lista (ou outro item se colocada a posição nos parênteses)
lista_animal.pop(1)
print(lista_animal)

#Remove - Retira item informado da lista
lista_animal.remove('lobo')
print(lista_animal)

#Tuplas
#Diferença para listas - Listas são mutáveis e tuplas não

tupla = (1, 10, 12, 14)
print(tupla)

#Len
print(len(tupla))
print(len(lista_animal))

#Conversão de lista em tupla
tupla_animal = tuple(lista_animal)
print(type(tupla_animal))
print(tupla_animal)

#Conversão de tupla em lista
lista_numerica = list(tupla)
print(type(lista_numerica))
print(lista_numerica)