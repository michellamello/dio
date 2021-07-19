a = int(input('Entre com o primeiro valor: '))
b = int(input('Entre com o segundo valor: '))

soma = a + b
subtracao = a - b
multiplicacao = a * b
divisao = a / b
resto = a % b

#print (type(soma))

#Melhor forma de imprimir, não precisa converter
resultado = 'Soma: {soma}.\nSubtração: {subtracao}.\nMultiplicação: {multiplicacao}.\nDivisão: {divisao}.\nResto da divisão: {resto}'.format(soma=soma, subtracao=subtracao, multiplicacao=multiplicacao, divisao=divisao, resto=resto)

print(resultado)

#Outra forma de imprimir
#print('Soma: ' + str(soma))
#print('Subtração: ' + str(subtracao))
#print('Multiplicação: ' + str(multiplicacao))
#print('Divisão: ' + str(divisao))
#print('Resto da divisão: ' + str(resto))

#x = 1

#soma2 = int(x) + 1
#print(soma2)