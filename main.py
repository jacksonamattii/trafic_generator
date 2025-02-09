from scapy.all import *
import random

# Nome do arquivo PCAP
pcap_filename = "random_network_anomalies.pcap"
packets = []

# Tráfego ICMP suspeito (Ping Flood)
for i in range(50):  # Aumentando o volume de pacotes
    packets.append(IP(dst="192.168.1.1") / ICMP())

# Tráfego TCP SYN Scan (tentativa de escaneamento de portas)
for _ in range(20):  # Aumentando a intensidade do scan
    port = random.choice([22, 80, 443, 3389, 8080, 53, 445])
    packets.append(IP(dst="192.168.1.2") / TCP(dport=port, flags="S"))

# Tráfego DNS suspeito (consulta para domínios estranhos e múltiplas requisições)
suspect_domains = ["malicious-domain.example", "phishing-site.com", "unknown123.xyz"]
for domain in suspect_domains:
    packets.append(IP(dst="8.8.8.8") / UDP(dport=53) / DNS(rd=1, qd=DNSQR(qname=domain)))

# Pacotes com TTL baixo (indicando traceroute ou manipulação maliciosa)
for i in range(10):  # Mais pacotes
    packets.append(IP(dst="192.168.1.3", ttl=random.randint(1, 3)) / TCP(dport=80, flags="S"))

# Tráfego HTTP simulado
for i in range(30):
    packets.append(IP(dst="192.168.1.4") / TCP(dport=80, sport=random.randint(1024, 65535), flags="PA") / Raw(load="GET /index.html HTTP/1.1\r\nHost: example.com\r\n\r\n"))

# Tráfego HTTPS simulado
for i in range(20):
    packets.append(IP(dst="192.168.1.5") / TCP(dport=443, sport=random.randint(1024, 65535), flags="PA") / Raw(load="ClientHello"))

# Tráfego FTP simulado (tentativa de login)
ftp_payloads = ["USER anonymous\r\n", "PASS guest\r\n", "USER admin\r\n", "PASS password123\r\n"]
for i in range(10):
    packets.append(IP(dst="192.168.1.6") / TCP(dport=21, sport=random.randint(1024, 65535), flags="PA") / Raw(load=random.choice(ftp_payloads)))

# Salvar os pacotes no arquivo PCAP
wrpcap(pcap_filename, packets)
print(f"Arquivo PCAP gerado: {pcap_filename}")