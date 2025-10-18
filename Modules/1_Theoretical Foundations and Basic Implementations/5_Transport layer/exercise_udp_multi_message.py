# exercise_udp_multi_message.py
# Sends 10 UDP messages to server (Exercise 2 solution)
# Run with udp_server.py
# Scientist note: Add delay or packet size variation for testing

import socket
import sys

try:
    client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    print("UDP client created")
    server_addr = ("127.0.0.1", 12345)
    # Send 10 messages
    for i in range(10):
        msg = f"Message {i}".encode()
        client.sendto(msg, server_addr)
        print(f"Sent: {msg.decode()}")
    # Optional: Receive responses (server may not reply to all)
    data, addr = client.recvfrom(1024)
    print(f"Received from {addr}: {data.decode()}")
except socket.error as e:
    print(f"Error: {e}")
finally:
    client.close()
