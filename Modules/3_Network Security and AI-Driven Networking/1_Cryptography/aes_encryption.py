# aes_encryption.py
# A Python script demonstrating symmetric encryption using AES
# Purpose: Encrypt and decrypt a message using the Fernet library (AES-128 in CBC mode)
# For aspiring scientists: This shows how symmetric encryption works in practice

from cryptography.fernet import Fernet


def main():
    print("=== Symmetric Encryption with AES ===")
    print("This script generates a key, encrypts a message, and decrypts it back.")

    # Generate a random symmetric key (128-bit AES key with HMAC for integrity)
    key = Fernet.generate_key()
    print("Generated Key:", key.decode())

    # Create a Fernet cipher object with the key
    cipher = Fernet(key)

    # Define a sample message
    message = "Hello, aspiring scientist! This is a secret message.".encode()
    print("Original Message:", message.decode())

    # Encrypt the message
    ciphertext = cipher.encrypt(message)
    print("Encrypted Ciphertext:", ciphertext)

    # Decrypt the ciphertext
    decrypted = cipher.decrypt(ciphertext)
    print("Decrypted Message:", decrypted.decode())

    # Verify the decryption
    if decrypted == message:
        print("Success: The decrypted message matches the original!")
    else:
        print("Error: Decryption failed.")


if __name__ == "__main__":
    main()
