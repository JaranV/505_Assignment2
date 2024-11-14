from scapy.all import IP, TCP, send
import random
import time

target_ip = "10.0.2.4"
target_port = 80

http_payload = (
    "GET / HTTP/1.1\r\n"
    "Host: 10.0.2.4\r\n"
    "User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36\r\n"
    "Connection: keep-alive\r\n"
    "Content-Type: application/x-www-form-urlencoded\r\n"
    "X-Payload: echo 'Simulated malicious command'\r\n"
    "\r\n"
)

for i in range(3):
    segment = http_payload[i*30:(i+1)*30]
    packet = IP(dst=target_ip)/TCP(dport=target_port, sport=random.randint(1024, 65535), flags="PA")/segment
    send(packet)
    time.sleep(random.uniform(0.5, 1.5))
