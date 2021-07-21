#Métodos, funções e classes

#def - Método

if __name__ == '__main__':
    def soma(a, b):
        return a + b # é uma função pois possui retorno. Se não tivesse, seria um método

    #Chamando uma função
    print(soma(1, 2))
    print(soma(3, 4))

    def subtracao(a, b):
        return a - b

    print(subtracao(10, 2))
    print(subtracao(30, 4))

    def multiplicacao (a, b):
        return a * b

    print(multiplicacao(10, 2))
    print(multiplicacao(30, 4))

    def divisao(a, b):
        return a / b

    print(divisao(10, 2))
    print(divisao(30, 4))

#Class - Classe

class Calculadora:
    def __init__(self, num1, num2):
        self.valor_a = num1
        self.valor_b = num2    

    def soma(self):
        return self.valor_a + self.valor_b

    def subtracao(self):
        return self.valor_a - self.valor_b

    def multiplicacao (self):
        return self.valor_a * self.valor_b

    def divisao(self):
        return self.valor_a / self.valor_b

#Instanciando a calculadora
if __name__ == '__main__':
    calculadora = Calculadora(10, 2)
    print(calculadora.valor_a)
    print(calculadora.valor_b)

    print(calculadora.soma())
    print(calculadora.subtracao())
    print(calculadora.multiplicacao())
    print(calculadora.divisao())
