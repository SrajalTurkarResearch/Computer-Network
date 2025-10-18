# diffie_hellman.py
# A Python script demonstrating Diffie-Hellman key exchange
# Purpose: Generate shared secret key over an insecure channel
# For aspiring scientists: Shows how two parties can agree on a secret without direct exchange

from cryptography.hazmat.primitives.asymmetric import dh
from cryptography.hazmat.primitives.kdf.hkdf import HKDF
from cryptography.hazmat.primitives import hashes


def main():
    print("=== Diffie-Hellman Key Exchange ===")
    print("This script simulates Alice and Bob creating a shared secret key.")

    # Generate DH parameters (prime modulus and generator)
    parameters = dh.generate_parameters(generator=2, key_size=2048)
    print("DH Parameters Generated (2048-bit)")

    # Alice generates her private and public keys
    alice_private = parameters.generate_private_key()
    alice_public = alice_private.public_key()
    print("Alice's Public Key Generated")

    # Bob generates his private and public keys
    bob_private = parameters.generate_private_key()
    bob_public = bob_private.public_key()
    print("Bob's Public Key Generated")

    # Alice and Bob exchange public keys and compute shared secret
    alice_shared = alice_private.exchange(bob_public)
    bob_shared = bob_private.exchange(alice_public)

    # Verify the shared secrets match
    print("Shared Key Match:", alice_shared == bob_shared)

    # Derive a symmetric key using HKDF for practical use
    derived_key = HKDF(
        algorithm=hashes.SHA256(), length=32, salt=None, info=b"handshake data"
    ).derive(alice_shared)
    print("Derived Symmetric Key (hex):", derived_key.hex())


if __name__ == "__main__":
    main()
