#Personalização de exceções

class Error(Exception):
    pass

class InputError(Error):
    def __init__(self, message):
        self.message = message
    

while True:
    try:
        x = int(input('Entre com uma nota de zero a dez: '))
        print(x)
        if x > 10:
            raise InputError('Nota não pode ser maior que dez.')
        elif x < 0:
            raise InputError('Nota não pode ser menor que zero.')
        break
    except ValueError:
        print('Valor inválido, um número deve ser digitado.')
    except InputError as ex:
        print(ex)
