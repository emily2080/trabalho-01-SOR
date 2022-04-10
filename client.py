import json
import socket

from functions import *
from units import *

HOST, PORT = 'localhost', 5000

sair = ''

while sair != 'sair':
    grandeza = mostra_menu_de_grandezas()
    unidade_escolhida_de = mostra_menu_unidades_de_medida_de(grandeza)
    unidade_escolhida_para = mostra_menu_unidades_de_medida_para(grandeza)
    
    valor = float(input('Valor: '))

    info = [
        grandeza,
        unidade_escolhida_de,
        valor,
        unidade_escolhida_para
    ]

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((HOST, PORT))

    s.send(json.dumps(info).encode('utf-8'))

    convertido = s.recv(1024).decode('utf-8')
    convertido = json.loads(convertido)

    print()
    print(f'{valor}{list(unidades.values())[info[0] - 1][info[1] - 1]} = {convertido}{list(unidades.values())[info[0] - 1][info[3] - 1]}')
    print()

    sair = str(input('Digite "sair" para sair do conversor\n\n>: '))

print('Saindo...\n')
