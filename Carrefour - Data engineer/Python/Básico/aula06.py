#Conjuntos

conjunto = {1, 2, 3, 4}

print(type(conjunto))
print(conjunto)

#Adição de elementos
conjunto.add(5)

print(conjunto)

#Remoção de elementos
conjunto.discard(2)

print(conjunto)

#União de conjuntos
conjunto = {1, 2, 3, 4, 5}
conjunto2 = {5, 6, 7, 8}
conjunto_uniao = conjunto.union(conjunto2)

print(conjunto_uniao)

#Intersecção de conjuntos
conjunto_interseccao = conjunto.intersection(conjunto2)

print(conjunto_interseccao)

#Diferença entre conjuntos
conjunto_diferenca = conjunto.difference(conjunto2)
conjunto_diferenca2 = conjunto2.difference(conjunto)

print(conjunto_diferenca)
print(conjunto_diferenca2)

#Diferença simétrica
conjunto_dif_simetrica = conjunto.symmetric_difference(conjunto2)

print(conjunto_dif_simetrica)

#Pertinência

#Subset - Subconjunto
conjunto_a = {1, 2, 3}
conjunto_b = {1, 2, 3, 4, 5}
conjunto_subset = conjunto_a.issubset(conjunto_b)

print(conjunto_subset)

#Superset - Superconjunto
conjunto_superset = conjunto_b.issuperset(conjunto_a)

print(conjunto_superset)

#Conversão lista para conjunto - Remoção rápida de duplicidades
lista = ['cachorro', 'cachorro', 'gato', 'gato', 'elefante']
conjunto_animais = set(lista)

print(conjunto_animais)

lista_animais = list(conjunto_animais)
print(lista_animais)
