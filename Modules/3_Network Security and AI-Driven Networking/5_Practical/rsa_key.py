# rsa_key.py
# Generates an RSA private key and prints it in PEM format.
# Core to asymmetric encryption in network security.

from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives import serialization

# Generate 2048-bit RSA private key
private_key = rsa.generate_private_key(public_exponent=65537, key_size=2048)

# Serialize to PEM
pem = private_key.private_bytes(
    encoding=serialization.Encoding.PEM,
    format=serialization.PrivateFormat.PKCS8,
    encryption_algorithm=serialization.NoEncryption(),
)

print(pem.decode("utf-8"))
print("RSA key generated. Use for encryption/decryption in secure protocols.")
