# tls_connection.py
# Purpose: Demonstrates a TLS/SSL secure connection to a website, showing how TLS works in practice.
# Use: Run this script to connect to a website (e.g., www.google.com) and print the TLS version and cipher used.
# Relevance: Understand TLS handshake and encryption for web security, a key protocol for secure communication.
# Requirements: Python 3, ssl, socket libraries (built-in).
# Note: This is a simple example for learning; real-world TLS involves more complexity.

import ssl
import socket


def connect_tls(hostname):
    """
    Connect to a website using TLS and print connection details.
    Args:
        hostname (str): The website to connect to (e.g., 'www.google.com').
    """
    try:
        # Create a TLS context (like setting up a secure phone line)
        context = ssl.create_default_context()

        # Create a socket (like a phone connection)
        with socket.create_connection((hostname, 443)) as sock:
            # Wrap the socket with TLS (like adding encryption to the call)
            with context.wrap_socket(sock, server_hostname=hostname) as ssock:
                print(f"Connected to {hostname}")
                print(
                    f"TLS Version: {ssock.version()}"
                )  # Shows TLS version (e.g., TLSv1.3)
                print(f"Cipher Used: {ssock.cipher()}")  # Shows encryption method
    except Exception as e:
        print(f"Error connecting to {hostname}: {e}")


if __name__ == "__main__":
    # Try connecting to a website
    connect_tls("www.google.com")

    # Exercise: Change the hostname to another secure site (e.g., 'www.wikipedia.org')
    # and observe the TLS version and cipher. What differences do you notice?

# Why This Matters for Scientists:
# - This code shows how TLS ensures confidentiality and authentication.
# - Experiment with different sites to see how ciphers vary, sparking research into cipher strength.
