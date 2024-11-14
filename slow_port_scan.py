import random
import time
from scapy.all import IP, TCP, sr1

target_ip = "10.0.2.4"
ports = [22, 80, 443, 8080]

for port in ports:
    packet = IP(dst=target_ip)/TCP(dport=port, flags="S")
    response = sr1(packet, timeout=1, verbose=0)

    delay = random.uniform(1, 5)
    time.sleep(delay)

    if response:
        if response.haslayer(TCP) and response[TCP].flags == "SA":
            print(f"Port {port} is open")
        elif response.haslayer(TCP) and response[TCP].flags == "RA":
            print(f"Port {port} is closed")
    else:
        print(f"Port {port} is filtered or unresponsive")
