# protocol_implementation.py
# Purpose: Implement a custom network protocol with client and server.
# Context: Part of Jupyter Notebook tutorial, Section 3 - Protocol Implementation.
# Use: Run server first (`python3 protocol_implementation.py server`), then client in another terminal.
# Note: Demonstrates a simple protocol with a custom header for research flexibility.

import socket
import struct
import sys
import time


def run_server(host="127.0.0.1", port=12345):
    """
    Server: Listens for client messages with a custom header.
    Header: Magic (2 bytes, 0xABCD), Length (2 bytes), Type (1 byte).
    Theory Link: Section 3.2 - Protocol Implementation in Jupyter Notebook.
    Analogy: Like a post office checking letter formats before delivery.
    """
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((host, port))
    server_socket.listen(1)
    print(f"Server listening on {host}:{port}")

    while True:
        try:
            conn, addr = server_socket.accept()
            print(f"Connected to {addr}")

            # Receive header (5 bytes)
            header = conn.recv(5)
            if len(header) != 5:
                print("Invalid header")
                conn.close()
                continue

            # Unpack: > (network byte order), H (2 bytes), B (1 byte)
            magic, length, msg_type = struct.unpack(">HHB", header)
            if magic != 0xABCD:
                print("Wrong magic number, ignoring")
                conn.close()
                continue

            # Receive payload
            payload = conn.recv(length).decode()
            print(f"Received message type {msg_type}: {payload}")

            # Send ACK
            conn.send(b"ACK: Message received")
            conn.close()

        except Exception as e:
            print(f"Server error: {e}")
            conn.close()


def run_client(host="127.0.0.1", port=12345, message="Hello, Server!", msg_type=1):
    """
    Client: Sends a message with a custom header to the server.
    """
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        client_socket.connect((host, port))

        # Create header: Magic=0xABCD, Length=len(message), Type=msg_type
        header = struct.pack(">HHB", 0xABCD, len(message), msg_type)
        client_socket.send(header + message.encode())

        # Receive response
        response = client_socket.recv(1024).decode()
        print(f"Server response: {response}")

    except Exception as e:
        print(f"Client error: {e}")
    finally:
        client_socket.close()


if __name__ == "__main__":
    print("Custom Protocol Demo for Network Scientists")
    print("=========================================")
    if len(sys.argv) < 2:
        print("Usage: python3 protocol_implementation.py [server|client]")
        sys.exit(1)

    mode = sys.argv[1].lower()
    if mode == "server":
        run_server()
    elif mode == "client":
        run_client()
    else:
        print("Invalid mode. Use 'server' or 'client'.")

    # Research Tip: Extend this protocol with encryption (see Jupyter Notebook Section 3.2).
    # Try adding checksums or testing in a simulated network (Section 4).
