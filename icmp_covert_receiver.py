from scapy.all import sniff, IP, ICMP

def extract_payload(packet):
    if packet.haslayer(ICMP) and packet[ICMP].type == 8:
        message = packet[ICMP].payload.load.decode(errors='ignore')
        print("Message:", message)

sniff(filter="icmp", prn=extract_payload, store=0)
