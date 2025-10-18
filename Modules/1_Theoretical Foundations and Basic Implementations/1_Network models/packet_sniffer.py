# packet_sniffer.py
# Captures and analyzes network packets to study layering (OSI/TCP/IP)
# Purpose: Understand real packet flow across layers
# Relevance: Packet analysis reveals L2 (Ethernet), L3 (IP), L4 (TCP/UDP) behavior
# Usage: Run with sudo (network access required); install Scapy: pip install scapy
# Warning: Ensure legal/ethical use on your own network

from scapy.all import sniff


def analyze_packet(packet):
    """Analyze packet to identify layer information."""
    print("\nPacket Summary:")
    if packet.haslayer("Ether"):
        print(
            f"L2 (Data Link): Source MAC={packet['Ether'].src}, Dest MAC={packet['Ether'].dst}"
        )
    if packet.haslayer("IP"):
        print(f"L3 (Network): Source IP={packet['IP'].src}, Dest IP={packet['IP'].dst}")
    if packet.haslayer("TCP"):
        print(
            f"L4 (Transport): TCP Port={packet['TCP'].sport} -> {packet['TCP'].dport}"
        )
    elif packet.haslayer("UDP"):
        print(
            f"L4 (Transport): UDP Port={packet['UDP'].sport} -> {packet['UDP'].dport}"
        )


def main():
    print("Capturing 5 packets... (Ctrl+C to stop)")
    # Sniff 5 packets and analyze each
    sniff(count=5, prn=analyze_packet)


if __name__ == "__main__":
    main()

# Research Insight: Packet sniffing aids cybersecurity research (e.g., detecting L3 spoofing).
# Example: Analyze traffic in a lab network to study DDoS patterns.
# Next Step: Filter packets by protocol (e.g., HTTP) for L7 analysis in experiments.
