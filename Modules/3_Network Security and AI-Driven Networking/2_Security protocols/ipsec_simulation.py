# ipsec_simulation.py
# Purpose: Simulates IPsec's ESP (Encapsulating Security Payload) encryption using AES.
# Use: Run to encrypt and decrypt a message, mimicking IPsec's data protection.
# Relevance: Understand how IPsec secures network-layer traffic, critical for VPNs and secure networks.
# Requirements: Python 3, cryptography library (install via `pip install cryptography`).
# Note: This is a simplified simulation; real IPsec includes packet headers and IKE.

from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
import os


def encrypt_decrypt_data(data, key, iv):
    """
    Encrypt and decrypt data using AES-CBC, simulating IPsec ESP.
    Args:
        data (bytes): Data to encrypt (e.g., b'Secret network data').
        key (bytes): 32-byte key for AES-256.
        iv (bytes): 16-byte initialization vector.
    Returns:
        tuple: (encrypted data, decrypted data).
    """
    # Pad data to multiple of 16 bytes (AES block size)
    padded_data = data + b"\x00" * (16 - len(data) % 16)

    # Set up AES cipher in CBC mode
    cipher = Cipher(algorithms.AES(key), modes.CBC(iv), backend=default_backend())

    # Encrypt
    encryptor = cipher.encryptor()
    encrypted = encryptor.update(padded_data) + encryptor.finalize()

    # Decrypt
    decryptor = cipher.decryptor()
    decrypted = decryptor.update(encrypted) + decryptor.finalize()

    return encrypted, decrypted.rstrip(b"\x00")


if __name__ == "__main__":
    # Generate random key and IV (in real IPsec, these come from IKE)
    key = os.urandom(32)  # 256-bit key
    iv = os.urandom(16)  # 128-bit IV

    # Data to protect
    data = b"Secret network data"

    # Run encryption/decryption
    encrypted, decrypted = encrypt_decrypt_data(data, key, iv)
    print(f"Original: {data.decode()}")
    print(f"Encrypted: {encrypted.hex()}")
    print(f"Decrypted: {decrypted.decode()}")

    # Exercise: Try different data inputs or key sizes (e.g., 16 bytes for AES-128).
    # How does padding affect the output?

# Why This Matters for Scientists:
# - Simulates IPsec's core encryption, helping you understand network-layer security.
# - Experiment with key sizes or modes (e.g., GCM) to research performance vs. security trade-offs.
