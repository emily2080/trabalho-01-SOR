import json
import socket

from functions import *
from units import *

HOST, PORT = 'localhost', 5000

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST, PORT))

while True:
    s.listen()

    clientsocket, endereco = s.accept()

    data = clientsocket.recv(1024)
    data = json.loads(data)

    tipo = list(unidades.keys())[data[0] - 1]

    if (tipo == 'distancia'):
        valor = distancia(data[1], data[2], data[3])
    elif (tipo == 'tempo'):
        valor = tempo(data[1], data[2], data[3])
    elif (tipo == 'velocidade'):
        valor = velocidade(data[1], data[2], data[3])
    elif (tipo == 'temperatura'):
        valor = temperatura(data[1], data[2], data[3])

    clientsocket.send(json.dumps(valor).encode('utf-8'))
    clientsocket.close()
