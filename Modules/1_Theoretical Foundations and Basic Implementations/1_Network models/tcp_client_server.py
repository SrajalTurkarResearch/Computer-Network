# tcp_client_server.py
# Simulates a TCP client-server connection (Transport Layer, TCP/IP Model)
# Purpose: Demonstrate reliable data transfer, a key concept in network models
# Relevance: TCP (L4) ensures error-free delivery, critical for scientific data (e.g., CERN experiments)
# Usage: Run server first, then client in separate terminal
# Install: No external libraries needed (uses built-in socket)

import socket


def run_server():
    """Server simulates receiving data at Transport Layer (TCP)."""
    # Create TCP socket (AF_INET for IPv4, SOCK_STREAM for TCP)
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # Bind to localhost:12345
    server.bind(("localhost", 12345))
    server.listen(1)  # Listen for 1 connection
    print("Server listening on port 12345...")

    # Accept client connection
    conn, addr = server.accept()
    print(f"Connected by {addr}")

    # Receive data (1024 bytes buffer)
    data = conn.recv(1024)
    print(f"Received: {data.decode()}")

    # Send acknowledgment (mimics TCP ACK)
    conn.send(b"ACK: Data received")
    conn.close()
    server.close()


def run_client():
    """Client simulates sending data at Transport Layer (TCP)."""
    # Create TCP socket
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # Connect to server
    client.connect(("localhost", 12345))

    # Send data
    message = "Hello from Transport Layer!"
    client.send(message.encode())

    # Receive acknowledgment
    response = client.recv(1024)
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

# Research Insight: TCP's reliability (retransmission, flow control) is vital for scientific data integrity.
# Example: Ensures no loss in genomic data uploads to NCBI servers.
# Next Step: Modify to measure latency (RTT) for L4 analysis in experiments.
