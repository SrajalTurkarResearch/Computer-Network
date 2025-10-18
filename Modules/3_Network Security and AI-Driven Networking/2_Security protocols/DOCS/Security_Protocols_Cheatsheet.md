# Security Protocols in Computer Networks: Cheatsheet

This cheatsheet is a quick-reference guide for the **Security Protocols in Computer Networks** tutorial, covering **TLS/SSL** , **IPsec** , **VPNs** , and **Formal Security Models** . It’s designed for aspiring scientists, summarizing key concepts, terms, code snippets, and tips in simple, clear language. Use it to review, take notes, or prepare for research and experiments. All information ties back to the tutorial, ensuring you have everything needed for your scientific journey.

---

## 1. Basics of Network Security

### Key Concepts

- **Network Security** : Protects data as it travels between computers, ensuring it’s private, unchanged, and available.
- **CIA+ Triad** :
- **Confidentiality** : Only authorized people see data (like a locked diary).
- **Integrity** : Data stays unchanged (like a sealed envelope).
- **Authentication** : Verifies identities (like showing ID).
- **Availability** : Data is accessible (like an open post office).
- **Extras** : Non-repudiation (proof of sending/receiving), Authorization (what you’re allowed to do).
- **Threats** :
- Eavesdropping: Listening to data.
- Man-in-the-Middle (MitM): Intercepting and faking communication.
- Denial of Service (DoS): Blocking access.
- Impersonation: Pretending to be someone else.
- Tampering: Changing data.
- Replay Attacks: Reusing old data.

### Quick Tips

- Analogy: Network security is like a secure mail system with locks, seals, and ID checks.
- Research Focus: Study how threats evolve (e.g., AI-driven attacks).

---

## 2. TLS/SSL: Keeping Web Data Safe

### Key Concepts

- **Purpose** : Secures web and email data (e.g., HTTPS, Gmail).
- **How It Works** :
- **Handshake** : Client and server agree on a secret key using:
  - Client Hello: Lists codes (e.g., AES-256).
  - Server Hello: Sends certificate (ID) and code choice.
  - Key Exchange: Shares a secret key (e.g., Diffie-Hellman).
  - Finished: Confirms secure setup.
- **Data Transfer** : Encrypts data with symmetric codes (e.g., AES), adds MAC for integrity.
- **Codes** :
- Asymmetric: RSA, Diffie-Hellman, ECDH (key sharing).
- Symmetric: AES-256, ChaCha20 (data encryption).
- Hashing: SHA-256, HMAC (integrity checks).
- **Math Example (Diffie-Hellman)** :
- Pick prime ( p = 23 ), number ( g = 5 ).
- Alice sends ( 5^6 \mod 23 = 8 ), Bob sends ( 5^{15} \mod 23 = 19 ).
- Shared key: ( 19^6 \mod 23 = 2 ) (Alice), ( 8^{15} \mod 23 = 2 ) (Bob).

### Code Snippet

```python
import ssl, socket
context = ssl.create_default_context()
with socket.create_connection(('www.google.com', 443)) as sock:
    with context.wrap_socket(sock, server_hostname='www.google.com') as ssock:
        print(ssock.version(), ssock.cipher())
```

### Quick Tips

- TLS 1.3 is fastest and safest; avoid old SSL.
- Research: Post-quantum TLS (e.g., Kyber).

---

## 3. IPsec: Protecting Network Traffic

### Key Concepts

- **Purpose** : Secures network-layer packets (e.g., for VPNs, IoT).
- **Components** :
- **AH** : Checks integrity and sender (no encryption).
- **ESP** : Encrypts data, checks integrity/sender.
- **IKE** : Shares keys securely.
- **Modes** :
- Transport: Encrypts data only.
- Tunnel: Encrypts entire packet, adds new header.
- **Math Example (HMAC)** :
- Hash data with a secret key to create a unique fingerprint.
- Example: HMAC-SHA256(data, key) ensures data hasn’t changed.

### Code Snippet

```python
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
import os
key, iv = os.urandom(32), os.urandom(16)
cipher = Cipher(algorithms.AES(key), modes.CBC(iv))
encryptor = cipher.encryptor()
data = b'Secret network data'
padded = data + b'\x00' * (16 - len(data) % 16)
encrypted = encryptor.update(padded) + encryptor.finalize()
print(encrypted.hex())
```

### Quick Tips

- ESP is more common than AH (includes encryption).
- Research: Lightweight IPsec for IoT devices.

---

## 4. VPNs: Creating Safe Connections

### Key Concepts

- **Purpose** : Creates encrypted tunnels over the internet (e.g., remote work, privacy).
- **Types** :
- Remote Access: One user to a network.
- Site-to-Site: Network to network.
- **Protocols** :
- OpenVPN: TLS-based, secure.
- L2TP/IPsec: Combines tunneling and encryption.
- WireGuard: Fast, uses ChaCha20, Curve25519.
- **Math Example (Curve25519)** :
- Uses elliptic curves for fast key sharing.
- Simpler, stronger than Diffie-Hellman.

### Code Snippet

```python
config = """
client
dev tun
proto udp
remote vpn.example.com 1194
cipher AES-256-GCM
"""
print(config)
```

### Quick Tips

- WireGuard is the future (simple, fast).
- Research: Scalable VPNs for millions of users.

---

## 5. Formal Security Models: Proving Safety

### Key Concepts

- **Purpose** : Use math to prove systems are secure.
- **Models** :
- **Bell-LaPadula** : Confidentiality (no read up, no write down).
  - Example: Secret user can’t read Top Secret files.
- **Biba** : Integrity (no write up, no read down).
  - Example: Trusted program can’t use untrusted data.
- **Clark-Wilson** : Transaction safety (e.g., banking).
- **Non-Interference** : High-security actions don’t affect low-security users.
- **Math Example (Lattice)** :
- Levels: Unclassified (0), Secret (1), Top Secret (2).
- Rule: User at Secret can read Unclassified/Secret, not Top Secret.

### Code Snippet

```python
levels = {'Unclassified': 0, 'Secret': 1, 'Top Secret': 2}
def can_read(user_level, file_level):
    return levels[user_level] >= levels[file_level]
print(can_read('Secret', 'Unclassified'))  # True
```

### Quick Tips

- Use Tamarin/ProVerif for verification.
- Research: Apply models to IoT or cloud systems.

---

## 6. Advanced Ideas & Research Paths

### Key Trends

- **QUIC** : Faster TLS for HTTP/3.
- **Post-Quantum Crypto** : Resists quantum attacks (e.g., CRYSTALS-Kyber).
- **Zero Trust** : Verify everyone, even with VPNs.

### Research Ideas

- AI for detecting IPsec anomalies.
- Lightweight protocols for smart devices.
- Formal verification for modern protocols.
- Privacy vs. surveillance in VPNs.

---

## 7. Quick Code References

### TLS Connection

```python
import ssl, socket
context = ssl.create_default_context()
sock = socket.create_connection(('www.google.com', 443))
ssock = context.wrap_socket(sock, server_hostname='www.google.com')
print(ssock.version())
```

### IPsec Simulation

```python
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
key, iv = os.urandom(32), os.urandom(16)
cipher = Cipher(algorithms.AES(key), modes.CBC(iv))
encryptor = cipher.encryptor()
data = b'Secret data'
padded = data + b'\x00' * (16 - len(data) % 16)
print(encryptor.update(padded).hex())
```

### VPN Config

```python
print("client\\ndev tun\\nproto udp\\nremote vpn.example.com 1194\\ncipher AES-256-GCM")
```

### Bell-LaPadula

```python
levels = {'Unclassified': 0, 'Secret': 1, 'Top Secret': 2}
def can_write(user_level, file_level): return levels[user_level] <= levels[file_level]
print(can_write('Secret', 'Top Secret'))  # True
```

---

## 8. Tools for Experimentation

- **Wireshark** : Analyze network traffic (TLS, IPsec).
- **OpenSSL** : Create/test TLS certificates.
- **StrongSwan** : Set up IPsec VPNs.
- **OpenVPN/WireGuard** : Build VPNs.
- **Tamarin/ProVerif** : Verify formal models.

---

## 9. What’s Missing in Other Tutorials

- **Math Details** : Step-by-step calculations (e.g., Diffie-Hellman).
- **Real-World Links** : Case studies like Heartbleed.
- **Research Focus** : Quantum threats, zero trust.
- **Hands-On** : Practical code and projects.

---

## 10. Next Steps

- **Experiment** : Run the .py files (e.g., tls_connection.py).
- **Read** : RFC 8446 (TLS 1.3), RFC 4301 (IPsec).
- **Research** : Post-quantum crypto, IoT security.
- **Connect** : Join IETF, attend Black Hat conferences.

This cheatsheet is your go-to reference for mastering security protocols. Keep it handy for quick reviews and research planning!
