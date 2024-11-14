from scapy.all import IP, ICMP, fragment, send

target_ip = "10.0.2.4"

base_packet = IP(dst=target_ip)/ICMP()

for i in range(10):
    fragments = fragment(base_packet, fragsize=8)
    for frag in fragments:
        send(frag)
