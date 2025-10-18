# secure_network_project.py
# Purpose: Simulates a secure client-server network with encryption, mimicking IPsec or VPN.
# Use: Run server first, then client in separate terminals. Share key manually.
# Relevance: Demonstrates secure communication, a core concept for network security research.
# Requirements: Python 3, cryptography library (install via `pip install cryptography`).
# Note: Simplified for learning; real systems use IKE or TLS for key exchange.

from cryptography.fernet import Fernet
import socket
import threading


def run_server(host="localhost", port=12345):
    """
    Server: Listens for encrypted messages and decrypts them.
    Args:
        host (str): Server host (default: localhost).
        port (int): Server port (default: 12345).
    """
    # Generate or use a shared key (in practice, use IKE or TLS)
    key = Fernet.generate_key()
    print(f"Server Key (share with client): {key.decode()}")
    f = Fernet(key)

    # Set up server socket
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.bind((host, port))
    sock.listen(1)
    print(f"Server listening on {host}:{port}")

    conn, addr = sock.accept()
    data = conn.recv(1024)
    decrypted = f.decrypt(data)
    print(f"Received and decrypted: {decrypted.decode()}")
    conn.close()
    sock.close()


def run_client(host="localhost", port=12345, key=None):
    """
    Client: Encrypts and sends a message to the server.
    Args:
        host (str): Server host.
        port (int): Server port.
        key (bytes): Shared key for encryption.
    """
    f = Fernet(key)
    message = b"Hello, secure world!"
    encrypted = f.encrypt(message)

    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect((host, port))
    sock.sendall(encrypted)
    sock.close()
    print(f"Client sent encrypted message: {encrypted.hex()}")


if __name__ == "__main__":
    # Run server in a separate thread
    server_thread = threading.Thread(target=run_server)
    server_thread.start()

    # Wait briefly, then run client with the same key
    import time

    time.sleep(1)
    key = input("Enter server key: ").encode()  # Manually input key from server output
    run_client(key=key)

    # Exercise: Modify to send different messages or use a real dataset (e.g., network logs).
    # Research how key exchange (e.g., Diffie-Hellman) could automate this.

# Why This Matters for Scientists:
# - Simulates secure network communication, a foundation for IPsec/VPN research.
# - Experiment with datasets or protocols to explore real-world applications.
