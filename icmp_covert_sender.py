from scapy.all import IP, ICMP, send
import time

target_ip = "10.0.2.4"
message = "Covert Channel Using ICMP"

for i in range(len(message)):
    packet = IP(dst=target_ip)/ICMP(type=8)/message[i]
    send(packet)
    time.sleep(0.1)
