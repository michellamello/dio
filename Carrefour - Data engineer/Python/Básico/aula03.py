a = int(input('Primeiro valor: '))
b = int(input('Segundo valor: '))
c = int(input('Terceiro valor: '))

#If/ Elif/ And
if a > b and a > c:
    print('O maior número é {}'.format(a))
elif a > a and b > c:
    print('O maior número é {}'.format(b))
else:
    print('O maior número é {}'.format(c))


#==
a = int(input('Entre com um valor: '))

resto = a % 2

if resto == 0:
    print('Número par')
else:
    print('Número ímpar')


#Or/ Not
a = int(input('Entre com o primeiro valor: '))
b = int(input('Entre com o segundo valor: '))

resto_a = a % 2
resto_b = b % 2

if resto_a == 0 or not resto_b > 0:
    print('Foi digitado um número par')
else:
    print('Nenhum númemro par foi digitado')

# <= / reforço If
a = int(input('Primeiro bimestre: '))
if a > 10:
    int(input('Você digitou uma data inválida. Digite novamente: '))

b = int(input('Segundo bimestre: '))
if b > 10:
    int(input('Você digitou uma data inválida. Digite novamente: '))

c = int(input('Terceiro bimestre: '))
if c > 10:
    int(input('Você digitou uma data inválida. Digite novamente: '))

d = int(input('Quarto bimestre: '))
if d > 10:
    int(input('Você digitou uma data inválida. Digite novamente: '))

media = (a + b + c + d) / 4

#if a < 10 and b <= 10 and c <= 10 and d <= 10:
#    media = (a + b + c + d) / 4
#else:
#    print('Foi informada uma nota errada')

print('Média: {}'.format(media))


