<div align="center">

# Basic Network Sniffer Using Python and Scapy

A simple cybersecurity project developed using Python and Scapy to capture and analyze live network traffic.

</div>

---

## Overview

This project is a basic network packet sniffer built using Python and the Scapy library. It captures live packets from the network interface and displays useful information such as source IP address, destination IP address, protocol type, and packet payload.

The project is designed for beginners to understand packet sniffing, traffic analysis, and network monitoring concepts used in cybersecurity.

---

## Features

- Real-time packet capturing
- Source and destination IP identification
- Protocol analysis
- Packet payload inspection
- Lightweight and beginner-friendly implementation
- Command-line based execution

---

## Technologies Used

- Python 3
- Scapy
- Kali Linux
- Virtual Environment (venv)

---

## Project Structure

```text
CodeAlpha_Network_Sniffer
│
├── network_sniffer.py
├── README.md
├── output
     ├──Network Sniffer Output1.jpeg
     ├──Network Sniffer Output2.jpeg
     ├──Network Sniffer Output3.jpeg

```

---

## Installation

### Clone the Repository

```bash
git clone https://github.com/yourusername/CodeAlpha_Network_Sniffer.git
cd CodeAlpha_Network_Sniffer
```

---

### Create Virtual Environment

```bash
python3 -m venv venv
```

---

### Activate Virtual Environment

Linux/macOS:

```bash
source venv/bin/activate
```

Windows:

```bash
venv\Scripts\activate
```

---

### Install Required Dependencies

```bash
pip install scapy
```

or

```bash
pip install -r requirements.txt
```

---

## Usage

Run the packet sniffer with administrator or root privileges.

Linux/macOS:

```bash
sudo python3 sniffer1.py
```

Windows:

```bash
python network_sniffer.py
```

---

## Program Code

```python
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
```

---

## Generating Network Traffic

To test the packet sniffer, generate network activity by:

```bash
ping google.com
```

or by browsing websites such as:

```text
google.com
youtube.com
github.com
```

---

## Sample Output

```text
=== New Packet Captured ===

Source IP      : 192.168.1.5
Destination IP : 142.250.183.14
Protocol       : 6

Payload:
b'GET / HTTP/1.1'
```

---

## Learning Outcomes

- Network Packet Analysis
- Packet Sniffing Techniques
- TCP/IP Fundamentals
- Python Scripting
- Cybersecurity Basics
- Traffic Monitoring Concepts

---

## Future Enhancements

- TCP and UDP filtering
- Packet logging support
- GUI-based network sniffer
- Advanced protocol analysis
- Traffic visualization dashboard
- Intrusion detection features

---

## Disclaimer

This project is developed strictly for educational and ethical cybersecurity purposes. Use packet sniffing tools only on networks that you own or have permission to monitor. Unauthorized packet capturing may violate legal and organizational policies.
