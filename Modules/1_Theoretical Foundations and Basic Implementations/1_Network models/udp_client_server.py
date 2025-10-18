# udp_client_server.py
# Simulates a UDP client-server connection (Transport Layer, TCP/IP Model)
# Purpose: Demonstrate fast, connectionless data transfer
# Relevance: UDP (L4) prioritizes speed, used in streaming or IoT sensor networks
# Usage: Run server first, then client in separate terminal
# Install: No external libraries needed (uses built-in socket)

import socket


def run_server():
    """Server simulates receiving data at Transport Layer (UDP)."""
    # Create UDP socket (AF_INET for IPv4, SOCK_DGRAM for UDP)
    server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    # Bind to localhost:12346
    server.bind(("localhost", 12346))
    print("UDP Server listening on port 12346...")

    # Receive data (1024 bytes buffer)
    data, addr = server.recvfrom(1024)
    print(f"Received from {addr}: {data.decode()}")

    # Send response
    server.sendto(b"UDP ACK: Data received", addr)
    server.close()


def run_client():
    """Client simulates sending data at Transport Layer (UDP)."""
    # Create UDP socket
    client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    # Send data to server
    message = "Hello from UDP Transport Layer!"
    client.sendto(message.encode(), ("localhost", 12346))

    # Receive response
    response, addr = client.recvfrom(1024)
    print(f"Server response: {response.decode()}")
    client.close()


if __name__ == "__main__":
    # Run server or client based on user input
    mode = input("Run as (server/client)? ").lower()
    if mode == "server":
        run_server()
    elif mode == "client":
        run_client()
    else:
        print("Invalid mode. Choose 'server' or 'client'.")

# Research Insight: UDP's low overhead suits real-time applications (e.g., video streaming, IoT).
# Example: Environmental sensors use UDP for fast, lightweight data transfer.
# Next Step: Compare TCP vs. UDP throughput in a simulated IoT experiment.
