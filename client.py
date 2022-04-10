import json
import socket

from functions import *
from units import *

HOST, PORT = 'localhost', 5000

if __name__ == '__main__':
    sair = ''

    while sair != 'sair':
        tipo_de_unidade_escolhida = mostra_menu_tipos_de_unidades_de_medida()
        unidade_escolhida_de = mostra_menu_unidades_de_medida_de(tipo_de_unidade_escolhida)
        
        valor = float(input('Valor: '))
        
        unidade_escolhida_para = mostra_menu_unidades_de_medida_para(tipo_de_unidade_escolhida)

        info = [
            tipo_de_unidade_escolhida,
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

        sair = str(input('Digite sair para sair do conversor\n\n>: '))
    
    print('Saindo...\n')
