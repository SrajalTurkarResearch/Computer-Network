# udp_server.py
# Demonstrates UDP mechanics: connectionless datagram sending with ports and checksums
# Run this first, then run udp_client.py in another terminal
# For your scientist journey: Modify to test packet loss or measure latency

import socket
import sys

# Create UDP socket (SOCK_DGRAM for datagrams)
try:
    server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    # Bind to localhost and port 12345 (like an address for UDP datagrams)
    server.bind(("127.0.0.1", 12345))
    print("UDP server running on port 12345")
except socket.error as e:
    print(f"Error setting up server: {e}")
    sys.exit(1)

# Receive and respond to a client message
try:
    # Buffer size 1024 bytes (typical for small messages)
    data, addr = server.recvfrom(1024)  # Wait for datagram
    print(f"Received from {addr}: {data.decode()}")
    # Send response back (no connection, just send to addr)
    server.sendto(b"Hello from UDP server!", addr)
    print(f"Sent response to {addr}")
except socket.error as e:
    print(f"Error receiving/sending: {e}")
finally:
    server.close()  # Free the port
