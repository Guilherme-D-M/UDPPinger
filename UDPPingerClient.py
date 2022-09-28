import sys, time
from socket import *

# Obtenha o nome do host e a porta do servidor como argumentos de linha de comando
                    
host = "127.0.0.1"
port = 1212
timeout = 1 # in second
 
# Create UDP client socket
# Observe o uso de SOCK_DGRAM para pacote de datagrama UDP
clientsocket = socket(AF_INET, SOCK_DGRAM)
# Definir o tempo limite do soquete como 1 segundo
clientsocket.settimeout(timeout)
# Número de sequência da mensagem de ping
ptime = 0  

# Ping por 10 vezes
while ptime < 10: 
    ptime += 1
    # Formate a mensagem a ser enviada
    data = "Ping " + str(ptime) + " " + time.asctime()
    
    try:
	# Horário de envio
        RTTb = time.time()
              
        string = data
        dataBytes = string.encode("utf-8")

        string = host
        hostBytes = string.encode("utf-8")

        # Envie o pacote UDP com a mensagem de ping
        clientsocket.sendto(dataBytes,(hostBytes, port))
        # Receber a resposta do servidor
        message, address = clientsocket.recvfrom(1024)
        
        # Hora de recebimento
        RTTa = time.time()
        # Exibir a resposta do servidor como uma saída

        message  = message.decode("utf-8")    
        print ("Reply from " + address[0] + ": " + message)
               
        # O tempo de ida e volta é a diferença entre o tempo enviado e recebido
        print ("RTT: " + str(RTTa - RTTb))
    except:
          # Servidor não responde
          # Suponha que o pacote está perdido
          print ("Request timed out.")
          continue
# Close the client socket
clientsocket.close()
 
