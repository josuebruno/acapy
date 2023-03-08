from scapy.all import ARP, Ether, srp
import os

# Define a rede que você deseja escanear
target_ip = "192.168.1.1/24"

# Cria um pacote ARP para enviar a todos os dispositivos na rede
arp = ARP(pdst=target_ip)

# Cria um pacote Ethernet para encapsular o pacote ARP
ether = Ether(dst="ff:ff:ff:ff:ff:ff")

# Combina os pacotes ARP e Ethernet
packet = ether/arp

# Envia o pacote e recebe a resposta
result = srp(packet, timeout=3, verbose=0)[0]

# Cria um dicionário para armazenar os endereços MAC e IP dos dispositivos encontrados
clients = []

# Percorre as respostas e adiciona os endereços MAC e IP ao dicionário
for sent, received in result:
    clients.append({'ip': received.psrc, 'mac': received.hwsrc})

# Imprime a lista de dispositivos encontrados
print("Dispositivos encontrados:")
print("IP\t\t\tMAC Address\n-----------------------------------------")
for client in clients:
    print(f"{client['ip']}\t\t{client['mac']}")

# Cria uma lista de nós e uma lista de conexões
nodes = []
connections = []

# Adiciona cada dispositivo como um nó na lista de nós
for client in clients:
    node = f"Node_{client['ip'].replace('.', '_')}"
    nodes.append(node)

# Adiciona as conexões entre os nós à lista de conexões
for i in range(len(clients)):
    for j in range(i + 1, len(clients)):
        connection = f"{nodes[i]} --> {nodes[j]}"
        connections.append(connection)

# Cria o código PlantUML para o diagrama UML
uml_code = "@startuml\n"
uml_code += "left to right direction\n"

# Adiciona cada nó ao diagrama UML
for node in nodes:
    uml_code += f"class {node} {{\n  {node}\n}}\n"

# Adiciona cada conexão ao diagrama UML
for connection in connections:
    uml_code += f"{connection}\n"

uml_code += "@enduml"

# Escreve o código PlantUML em um arquivo
with open("topology.puml", "w") as file:
    file.write(uml_code)

# Converte o arquivo PlantUML em um arquivo de imagem
os.system("java -jar plantuml.jar topology.puml")
