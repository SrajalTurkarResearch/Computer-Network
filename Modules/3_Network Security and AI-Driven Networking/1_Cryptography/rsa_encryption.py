# rsa_encryption.py
# A Python script demonstrating asymmetric encryption using RSA
# Purpose: Generate RSA key pair, encrypt with public key, decrypt with private key
# For aspiring scientists: Shows how public/private keys enable secure communication

from cryptography.hazmat.primitives.asymmetric import rsa, padding
from cryptography.hazmat.primitives import hashes


def main():
    print("=== Asymmetric Encryption with RSA ===")
    print("This script generates RSA keys, encrypts a message, and decrypts it back.")

    # Generate a 2048-bit RSA private key
    private_key = rsa.generate_private_key(public_exponent=65537, key_size=2048)
    public_key = private_key.public_key()
    print("RSA Key Pair Generated (2048-bit)")

    # Define a sample message
    message = "Top secret research data!".encode()
    print("Original Message:", message.decode())

    # Encrypt with public key using OAEP padding
    ciphertext = public_key.encrypt(
        message,
        padding.OAEP(
            mgf=padding.MGF1(algorithm=hashes.SHA256()),
            algorithm=hashes.SHA256(),
            label=None,
        ),
    )
    print("Encrypted Ciphertext (hex):", ciphertext.hex())

    # Decrypt with private key
    plaintext = private_key.decrypt(
        ciphertext,
        padding.OAEP(
            mgf=padding.MGF1(algorithm=hashes.SHA256()),
            algorithm=hashes.SHA256(),
            label=None,
        ),
    )
    print("Decrypted Message:", plaintext.decode())

    # Verify the decryption
    if plaintext == message:
        print("Success: The decrypted message matches the original!")
    else:
        print("Error: Decryption failed.")


if __name__ == "__main__":
    main()
