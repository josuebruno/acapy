Script de Escaneamento de Rede e Criação de Topologia em UML
Este é um script em Python que usa a biblioteca Scapy para escanear uma rede em busca de dispositivos conectados e, em seguida, cria uma topologia UML para esses dispositivos usando o código PlantUML gerado pelo script.

Como Usar
Certifique-se de ter o Python e a biblioteca Scapy instalados no seu computador.
Baixe o script para o seu computador.
Abra o terminal ou prompt de comando e navegue até o diretório onde o script foi baixado.
Execute o script usando o comando python network_topology.py.
O script irá escanear a rede e criar um arquivo "topology.png" contendo a topologia em UML dos dispositivos encontrados.
Note que o script assume que o arquivo "plantuml.jar" está no diretório de trabalho atual. Se o arquivo estiver em um diretório diferente, você precisará modificar o script para especificar o caminho correto para o arquivo.

Funcionamento
O script funciona da seguinte maneira:

Define a rede que se deseja escanear.
Cria um pacote ARP para enviar a todos os dispositivos na rede.
Cria um pacote Ethernet para encapsular o pacote ARP.
Combina os pacotes ARP e Ethernet.
Envia o pacote e recebe a resposta.
Armazena os endereços MAC e IP dos dispositivos encontrados em um dicionário.
Cria uma lista de nós e uma lista de conexões com base nos dispositivos encontrados.
Gera o código PlantUML para o diagrama UML.
Escreve o código PlantUML em um arquivo "topology.puml".
Chama o programa PlantUML para converter o código em um arquivo de imagem "topology.png".
Requisitos
Python
Biblioteca Scapy
PlantUML
Limitações
Este script pode não detectar todos os dispositivos na rede, dependendo das configurações de segurança e dos recursos de rede disponíveis.

Contribuindo
Este script é um projeto de código aberto e contribuições são bem-vindas. Sinta-se à vontade para criar pull requests para correções ou melhorias.
