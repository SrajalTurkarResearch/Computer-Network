# udp_client.py
# Demonstrates UDP client: Sends a datagram, receives response
# Run after udp_server.py in another terminal
# Scientist note: Extend to send multiple messages or test with real network

import socket
import sys

# Create UDP socket
try:
    client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    print("UDP client created")
except socket.error as e:
    print(f"Error creating socket: {e}")
    sys.exit(1)

# Send message to server
try:
    server_addr = ("127.0.0.1", 12345)  # Server address and port
    client.sendto(b"Hello UDP!", server_addr)  # Send datagram
    print("Sent message to server")
    # Wait for response
    data, addr = client.recvfrom(1024)
    print(f"Received from {addr}: {data.decode()}")
except socket.error as e:
    print(f"Error in communication: {e}")
finally:
    client.close()
