from scapy.all import IP, TCP, fragment, send

target_ip = "10.0.2.4"
target_port = 80

base_packet = IP(dst=target_ip)/TCP(dport=target_port, flags="S")

for i in range(10):
    fragments = fragment(base_packet, fragsize=8)
    for frag in fragments:
        send(frag)
