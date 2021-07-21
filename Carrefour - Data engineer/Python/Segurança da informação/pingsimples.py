import os #Importa o módulo ou biblioteca os (integra os programas e recursos do sistema operacional)

print('#' * 60) #Imprime # 60 vezes
ip_ou_host = input('Digite o IP ou host a ser verificado: ') #Cria uma variável que vai receber do usuário um IP ou host

print('-' * 60) #Imprime - 60 vezes
os.system('ping -c 6 {}'.format(ip_ou_host)) #Chama o método system da biblioteca os - comando ping (-c é o número de pacotes)
print('-' * 60) #Imprime - 60 vezes