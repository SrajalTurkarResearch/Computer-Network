# Cryptography Cheatsheet for Computer Networks

This cheatsheet summarizes key concepts, formulas, code snippets, and tips from the Cryptography in Computer Networks tutorial, designed for quick reference by aspiring scientists. It’s concise, clear, and beginner-friendly, covering symmetric encryption, asymmetric encryption, and Diffie-Hellman key exchange, with research-oriented insights.

## 1. Key Concepts

- **Cryptography** : Securing information by transforming plaintext into ciphertext.
- **Goals** :
- Confidentiality: Only authorized parties read the message.
- Integrity: Message isn’t altered.
- Authentication: Verifies sender/receiver identity.
- Non-repudiation: Sender can’t deny sending the message.
- **Symmetric Encryption** : One key for encryption and decryption.
- **Asymmetric Encryption** : Public key encrypts, private key decrypts.
- **Diffie-Hellman (DH)** : Creates a shared secret key over an insecure channel.

## 2. Symmetric Encryption

- **Definition** : Uses a single key to lock and unlock data.
- **Algorithms** :
- **AES** : 128/192/256-bit keys, block cipher, used in HTTPS, VPNs.
- **DES** : 56-bit key, outdated due to small key size.
- **Blowfish** : Up to 448-bit keys, good for lightweight systems.
- **Math** :
- Encryption: ( \text{Ciphertext} = \text{Algorithm}(\text{Plaintext}, \text{Key}) )
- Decryption: ( \text{Plaintext} = \text{Reverse Algorithm}(\text{Ciphertext}, \text{Key}) )
- **Code Snippet (AES with Python)** :

```python
  from cryptography.fernet import Fernet
  key = Fernet.generate_key()
  cipher = Fernet(key)
  message = "Hello!".encode()
  ciphertext = cipher.encrypt(message)
  decrypted = cipher.decrypt(ciphertext)
```

- **Pros** : Fast, great for large data.
- **Cons** : Key sharing is risky.
- **Tip** : Use AES-256 for strong security; ensure secure key distribution.

## 3. Asymmetric Encryption

- **Definition** : Uses a public key to encrypt and a private key to decrypt.
- **Algorithms** :
- **RSA** : Based on prime factorization, 2048/4096-bit keys.
- **ECC** : Based on elliptic curves, 256–521-bit keys, efficient.
- **Math (RSA)** :
- Key Generation:
  - Choose primes ( p, q ), compute ( n = p \times q ), ( \phi(n) = (p-1)(q-1) ).
  - Pick public ( e ), compute private ( d ) where ( d \times e \mod \phi(n) = 1 ).
- Encryption: ( \text{Ciphertext} = \text{Plaintext}^e \mod n )
- Decryption: ( \text{Plaintext} = \text{Ciphertext}^d \mod n )
- **Code Snippet (RSA with Python)** :

```python
  from cryptography.hazmat.primitives.asymmetric import rsa, padding
  from cryptography.hazmat.primitives import hashes
  private_key = rsa.generate_private_key(65537, 2048)
  public_key = private_key.public_key()
  message = "Secret!".encode()
  ciphertext = public_key.encrypt(message, padding.OAEP(mgf=padding.MGF1(hashes.SHA256()), algorithm=hashes.SHA256(), label=None))
  plaintext = private_key.decrypt(ciphertext, padding.OAEP(mgf=padding.MGF1(hashes.SHA256()), algorithm=hashes.SHA256(), label=None))
```

- **Pros** : Secure key exchange, enables signatures.
- **Cons** : Slower, private key must be protected.
- **Tip** : Use ECC for mobile devices; combine with AES for hybrid systems.

## 4. Diffie-Hellman Key Exchange

- **Definition** : Two parties create a shared secret key over an insecure channel.
- **Components** :
- Prime ( p ), generator ( g ).
- Private keys (( a, b )), public keys (( A = g^a \mod p ), ( B = g^b \mod p )).
- Shared secret: ( S = B^a \mod p = A^b \mod p ).
- **Math** :
- Alice: ( A = g^a \mod p ), sends ( A ).
- Bob: ( B = g^b \mod p ), sends ( B ).
- Shared secret: ( S = g^{ab} \mod p ).
- **Code Snippet (DH with Python)** :

```python
  from cryptography.hazmat.primitives.asymmetric import dh
  parameters = dh.generate_parameters(generator=2, key_size=2048)
  alice_private = parameters.generate_private_key()
  alice_public = alice_private.public_key()
  bob_private = parameters.generate_private_key()
  bob_public = bob_private.public_key()
  alice_shared = alice_private.exchange(bob_public)
  bob_shared = bob_private.exchange(alice_public)
```

- **Pros** : Secure key creation without direct sharing.
- **Cons** : Vulnerable to man-in-the-middle without authentication.
- **Tip** : Use with digital signatures for authentication.

## 5. Hybrid Cryptography

- **Definition** : Combines asymmetric encryption (for key exchange) and symmetric encryption (for data).
- **Example** : TLS uses RSA/DH to share an AES key, then AES for data.
- **Tip** : Essential for real-world systems like HTTPS.

## 6. Common Attacks

- **Brute Force** : Guess all keys.
- **Fix** : Use large keys (e.g., 256-bit AES).
- **Man-in-the-Middle (MITM)** : Impersonate a party.
- **Fix** : Use certificates or signatures.
- **Side-Channel** : Exploit physical leaks (e.g., power usage).
- **Fix** : Use constant-time algorithms.
- **Tip** : Regularly rotate keys and use strong algorithms.

## 7. Real-World Applications

- **HTTPS** : RSA/DH for key exchange, AES for data.
- **WhatsApp** : Signal Protocol with DH and AES.
- **Bitcoin** : ECC for signatures and wallet addresses.
- **VPNs** : DH for key setup, AES for traffic.

## 8. Research Directions

- **Post-Quantum Cryptography** : Develop lattice-based algorithms (e.g., Kyber).
- **Homomorphic Encryption** : Compute on encrypted data.
- **Side-Channel Defenses** : Design constant-time algorithms.
- **AI Integration** : Use AI for key management or attack detection.
- **Tip** : Explore NIST PQC standards and IACR conferences.

## 9. Quick Code Reference

- **Install Libraries** :

```bash
  pip install cryptography matplotlib networkx
```

- **Visualize Symmetric Flow** :

```python
  import networkx as nx
  import matplotlib.pyplot as plt
  G = nx.DiGraph()
  G.add_edges_from([('Plaintext', 'Encrypt with Key'), ('Encrypt with Key', 'Ciphertext'), ('Ciphertext', 'Decrypt with Key'), ('Decrypt with Key', 'Plaintext')])
  pos = nx.spring_layout(G)
  nx.draw(G, pos, with_labels=True, node_color='lightblue', node_size=2000, font_size=10)
  plt.title('Symmetric Encryption Flow')
  plt.show()
```

## 10. Tips for Scientists

- Experiment with key sizes to understand performance vs. security trade-offs.
- Read “Applied Cryptography” by Bruce Schneier.
- Join Crypto Stack Exchange for community support.
- Stay updated on quantum computing developments.
