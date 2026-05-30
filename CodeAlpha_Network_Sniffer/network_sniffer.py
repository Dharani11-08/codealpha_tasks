from scapy.all import sniff, IP, Raw

def packet_callback(packet):
    print("\n=== New Packet Captured ===")

    if packet.haslayer(IP):
        print(f"Source IP      : {packet[IP].src}")
        print(f"Destination IP : {packet[IP].dst}")
        print(f"Protocol       : {packet[IP].proto}")

    if packet.haslayer(Raw):
        print("Payload:")
        print(packet[Raw].load)

print("Starting Packet Capture...")
sniff(prn=packet_callback, store=False)
