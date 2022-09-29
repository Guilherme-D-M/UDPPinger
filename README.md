# UDPPinger

Tarefa desenvolvida na disciplina de redes pelo professor Marcos Courino no curso Análise e desenvolvimento de Sistemas no IFRS.

Nesta tarefa de programação, foi escrito um programa ping do cliente em Python. O cliente envia uma mensagem ping simples a um servidor, recebe uma mensagem pong correspondente de volta do servidor e determina o atraso entre o momento em que o cliente enviou a mensagem ping e recebeu a mensagem pong.
Esse atraso é denominado tempo de viagem de ida e volta (round-trip time — RTT). A funcionalidade oferecida pelo cliente e servidor é semelhante à fornecida pelo programa ping padrão, disponível nos sistemas operacionais modernos. Porém, os programas ping padrão usam o Internet Control Message Protocol (ICMP). Aqui, criamos um programa ping baseado em UDP, fora do padrão (porém simples!).
O programa ping envia 10 mensagens ping ao servidor de destino por meio de UDP. Para cada mensagem, o cliente determina e imprimir o RTT quando a mensagem pong correspondente for retornada. 
Como o UDP é um protocolo não confiável, um pacote enviado pelo cliente ou servidor poderá ser perdido. Por esse motivo, o cliente não espera indefinidamente por uma resposta a uma mensagem ping.
O cliente espera até 1 s por uma resposta do servidor; se nenhuma resposta for recebida, o cliente considera que o pacote foi perdido e imprime uma mensagem de acordo.
