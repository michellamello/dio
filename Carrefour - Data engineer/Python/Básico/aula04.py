#For
a = int(input('Entre com um número: '))

div = 0

for x in range(1, a + 1):
    resto = a % x
    if resto == 0:
        div += 1

if div == 2:
    print('Número {} é primo'.format(a))

else:
    print('Número {} não é primo'.format(a))

#For dentro de for
a = int(input('Entre com um valor: '))

for num in range(a + 1):
    div = 0

    for x in range(1, num + 1):
        resto = num % x
        if resto == 0:
            div += 1

    if div == 2:
        print(num)

#While
a = 0

while a < 10:
    print(a)
    a += 1

nota = int(input('Entre com a nota: '))

while nota > 10 or nota < 0:
    nota = int(input('Nota inválida. Entre com a nota correta: '))
    print(nota)
