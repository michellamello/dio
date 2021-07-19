class Televisao:
    def __init__(self):
        self.ligada = False
        self.canal = 2

    def power(self):
        if self.ligada:
            self.ligada = False
        else:
            self.ligada = True

    def aumenta_canal(self):
        if self.ligada:
            self.canal += 1

    def diminui_canal(self):
        if self.ligada:
            self.canal -= 1

if __name__ == '__main__': #Executa apenas se for chamado de dentro do módulo (mesmo arquivo .py)
    televisao = Televisao()
    print(televisao.ligada)
    televisao.power()
    print(televisao.ligada)
    televisao.power()
    print(televisao.ligada)

    televisao.power()
    print(televisao.ligada)

    print('Canal: {}'.format(televisao.canal))
    televisao.aumenta_canal()
    televisao.aumenta_canal()
    print('Canal: {}'.format(televisao.canal))

    televisao.diminui_canal()
    print('Canal: {}'.format(televisao.canal))