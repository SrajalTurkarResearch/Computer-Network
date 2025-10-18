# packet_analysis.py
# Purpose: Capture and analyze network packets using Scapy.
# Context: Part of the Jupyter Notebook tutorial for aspiring network scientists.
# Use: Run with Python 3, ensure Scapy is installed (`pip install scapy`).
# Note: Requires root/admin privileges for packet capture (e.g., `sudo python3 packet_analysis.py`).

from scapy.all import *  # Import Scapy for packet manipulation
import sys


def analyze_packets(count=5):
    """
    Capture and analyze a specified number of packets.
    Theory Link: Section 2 of Jupyter Notebook - Packet Analysis.
    Analogy: Like a detective examining letters to understand communication.
    """
    print(f"Capturing {count} packets...")
    try:
        # Capture packets (count specifies how many)
        packets = sniff(count=count, filter="tcp port 80 or udp port 53")
        # Filter: TCP port 80 (HTTP, web traffic) or UDP port 53 (DNS, name lookups)

        print("\nSummary of captured packets:")
        packets.summary()  # Show basic info about each packet

        # Detailed analysis for each packet
        print("\nDetailed analysis:")
        for i, packet in enumerate(packets):
            print(f"\nPacket {i+1}:")
            if IP in packet:
                print(f"  Source IP: {packet[IP].src}")
                print(f"  Destination IP: {packet[IP].dst}")
            if TCP in packet:
                print(
                    f"  Protocol: TCP, Source Port: {packet[TCP].sport}, Dest Port: {packet[TCP].dport}"
                )
            if UDP in packet:
                print(
                    f"  Protocol: UDP, Source Port: {packet[UDP].sport}, Dest Port: {packet[UDP].dport}"
                )
            if packet.haslayer(Raw):
                print(
                    f"  Payload: {packet[Raw].load[:20]}..."
                )  # Show first 20 bytes of payload

    except PermissionError:
        print("Error: Run this script with sudo/admin privileges.")
        sys.exit(1)
    except Exception as e:
        print(f"Error during capture: {e}")
        sys.exit(1)


def visualize_packet_counts(packets):
    """
    Create a simple count of packet types (TCP vs UDP).
    Theory Link: Section 2.3 - Visualizations in Jupyter Notebook.
    """
    tcp_count = sum(1 for pkt in packets if TCP in pkt)
    udp_count = sum(1 for pkt in packets if UDP in pkt)
    print(f"\nPacket Type Counts: TCP={tcp_count}, UDP={udp_count}")


if __name__ == "__main__":
    print("Packet Analysis Demo for Network Scientists")
    print("=========================================")
    # Capture 5 packets as a demo
    packets = sniff(count=5, filter="tcp port 80 or udp port 53")
    analyze_packets(count=5)
    visualize_packet_counts(packets)

    # Research Tip: Experiment with different filters (e.g., 'arp' for ARP spoofing detection).
    # See Jupyter Notebook Section 2 for advanced analysis like detecting malware beaconing.
