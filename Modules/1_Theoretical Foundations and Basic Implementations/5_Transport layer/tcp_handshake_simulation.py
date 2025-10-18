# tcp_handshake_simulation.py
# Simulates TCP handshake (SYN, SYN-ACK, ACK) using Scapy
# Requires Scapy: pip install scapy
# Scientist note: Modify SEQ/ACK numbers or add packet loss for research

from scapy.all import *
import sys

try:
    # Craft a SYN packet (client to server)
    ip = IP(src="192.168.1.1", dst="192.168.1.2")  # Simulated IPs
    tcp = TCP(sport=1234, dport=80, flags="S", seq=100)  # SYN flag, initial SEQ
    syn_packet = ip / tcp
    print("SYN packet:")
    syn_packet.show()

    # Simulate SYN-ACK response (server to client)
    syn_ack = IP(src="192.168.1.2", dst="192.168.1.1") / TCP(
        sport=80, dport=1234, flags="SA", seq=300, ack=101
    )
    print("\nSYN-ACK packet:")
    syn_ack.show()

    # Simulate ACK (client confirms)
    ack = IP(src="192.168.1.1", dst="192.168.1.2") / TCP(
        sport=1234, dport=80, flags="A", seq=101, ack=301
    )
    print("\nACK packet:")
    ack.show()

except ImportError:
    print("Install Scapy: pip install scapy")
    sys.exit(1)
except Exception as e:
    print(f"Error: {e}")
    sys.exit(1)
