# exercise_rsa.py
# Exercise: RSA encryption calculation.
# Encrypts message m=5 with e=3, n=33.

# Modular exponentiation
c = pow(5, 3, 33)
print(f"Encrypted ciphertext: {c}")

print("Solution: 5^3 = 125, 125 mod 33 = 26. Verify decryption with private key.")
