# UDPPingerServer.py
import random
from socket import *
# Create a UDP socket
# Observe o uso de SOCK_DGRAM para pacotes UDP
serverSocket = socket(AF_INET, SOCK_DGRAM)
# Atribuir endereço IP e número de porta ao soquete
serverSocket.bind(('', 1212))

while True:
    # Gerar número aleatório no intervalo de 0 a 10
    rand = random.randint(0, 10)

    # Receba o pacote do cliente junto com o endereço de onde ele está vindo
    message, address = serverSocket.recvfrom(1024)
    
    # Capitalize a mensagem do cliente
    message = message.upper()

    # Se rand for menor que 4, consideramos o pacote perdido e não respondemos
    if rand < 4:
        continue
#Caso contrário, o servidor responde
    serverSocket.sendto(message, address)