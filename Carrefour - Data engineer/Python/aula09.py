#Leitura e escrita, manipulação e movimentação de arquivos

import shutil

def escrever_arquivo(texto):
    arquivo = open('../teste.txt', 'w')
    arquivo.write(texto)
    arquivo.close()

    
def atualizar_arquivo(nome_arquivo, texto):
    arquivo = open(nome_arquivo, 'a')
    arquivo.write(texto)
    arquivo.close()

def ler_arquivo(nome_arquivo):
    diretorio = '../'
    arquivo = open(diretorio + nome_arquivo, 'r')
    texto = arquivo.read()
    #print(texto)

def media_notas(nome_arquivo):
    arquivo = open(nome_arquivo, 'r')
    aluno_nota = arquivo.read()
    aluno_nota = aluno_nota.split('\n')
    #print(aluno_nota)
    lista_media = []
    for x in aluno_nota:
    #   print(x)
        lista_notas = x.split(',')
        #print(lista_notas)
        aluno = lista_notas[0]
        #print(aluno)
        lista_notas.pop(0)
        media = lambda notas: sum([int(i) for i in notas]) / 4
        lista_media.append({aluno: media(lista_notas)})
        #print(media(lista_notas))
    return lista_media

#Mover e copiar arquivo

def copia_arquivo(nome_arquivo):
    shutil.copy(nome_arquivo, '../')

def move_arquivo(nome_arquivo):
    shutil.move(nome_arquivo, '../')

if __name__ == '__main__':
    move_arquivo('notas.txt')
    #copia_arquivo('notas.txt')
    # lista_media = media_notas('notas.txt')
    #print(lista_media)
    #escrever_arquivo('Primeira linha.\n')
    #atualizar_arquivo('notas.txt', aluno)
    #ler_arquivo('teste.txt')