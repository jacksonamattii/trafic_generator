# PCAP Traffic Generation

Este repositório contém um script em Python que gera um arquivo de captura de pacotes (PCAP) contendo tráfego de rede simulado. O objetivo é fornecer um dataset para análise de tráfego no Wireshark ou outras ferramentas de monitoramento de rede.

## 📌 Funcionalidades
O script gera pacotes simulados contendo diferentes tipos de tráfego:
- **Ping Flood (ICMP)**
- **Escaneamento de portas (TCP SYN Scan)**
- **Consultas DNS suspeitas**
- **Pacotes com TTL baixo** (indicação de traceroute ou tráfego manipulado)
- **Requisições HTTP e HTTPS simuladas**
- **Tentativas de login FTP**

## 🚀 Como Usar

### 1️⃣ Instalar Dependências
O script utiliza a biblioteca `scapy`. Se ainda não tiver instalada, execute:
```bash
pip install scapy
````

### 2️⃣ Executar o Script

Basta rodar o script em um ambiente Python:
python generate_pcap.py
Isso criará um arquivo random_network_anomalies.pcap, que pode ser analisado no Wireshark:
wireshark random_network_anomalies.pcap


### 📂 Estrutura do Projeto:

/
├── generate_pcap.py  # Script de geração de tráfego
├── random_network_anomalies.pcap  # Arquivo gerado com tráfego simulado
├── README.md  # Documentação do projeto

### 🔍 Análise no Wireshark
Após abrir o arquivo .pcap no Wireshark, é possível:

Filtrar pacotes específicos usando expressões como icmp, tcp.flags.syn == 1, dns.qry.name contains "malicious-domain", etc.
Identificar padrões suspeitos e anomalias na rede.
📜 Licença
Este projeto é distribuído sob a licença MIT. Sinta-se à vontade para modificar e contribuir!
