# tls_client.py
# Establishes a TLS connection to a server and prints the TLS version.
# Practical example of secure protocol implementation.

import socket
import ssl

# Create SSL context
context = ssl.create_default_context()

# Connect to example server
with socket.create_connection(("www.example.com", 443)) as sock:
    with context.wrap_socket(sock, server_hostname="www.example.com") as ssock:
        version = ssock.version()
        print(f"TLS version: {version}")

print("TLS connection successful. This demonstrates secure web communication.")
