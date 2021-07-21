import os
import time

with open('hosts.txt')as file:
    dump = file.read()
    dump = dump.splitlines()

    for ip in dump:
        print('Verificando o IP: {}'.format(ip))
        print('-' * 60)
        os.system('ping -c 6 {}'.format(ip))
        print('-' * 60)
        time.sleep(5)
    