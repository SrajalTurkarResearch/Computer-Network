# Cheatsheet: Secure Protocol Implementation & AI-Driven Networking

_A concise reference on network fundamentals, secure protocols, and AI-based optimization and security. Use for quick study, notes, or as a launchpad for projects and innovation._

---

## Fundamentals of Computer Networks

- **Network Types:**

  - _PAN_: Bluetooth
  - _LAN_: Wi-Fi
  - _MAN_: Metropolitan (city)
  - _WAN_: Internet
  - _SAN_: Storage

- **Topologies:**

  - Bus (linear, can have collisions)
  - Star (central hub, easy to scale)
  - Ring (loop, equal access)
  - Mesh (redundant; #edges=N(N-1)/2)
  - Tree (hierarchical)
  - Hybrid

- **OSI Model Layers:**

  1. **Physical**: Bits, cables
  2. **Data Link**: Frames, MAC
  3. **Network**: Packets, IP routing
  4. **Transport**: TCP (reliable; AIMD: rate +=1 or /=2), UDP (fast)
  5. **Session**: Connections
  6. **Presentation**: Formatting, encryption
  7. **Application**: HTTP, FTP

- **Key Formula:**  
  Shannon Capacity:  
  `C = B log₂(1 + SNR)`  
  _Example_: If B=100MHz, SNR=30dB → ≈1Gbps

- **Tip:**  
  Use [NetworkX](https://networkx.org/) in Python for network simulation:
  ```python
  import networkx as nx
  nx.star_graph(5)
  ```

---

## Secure Protocol Implementation

- **CIA Triad:**

  - _Confidentiality_: Encryption
  - _Integrity_: Hashing
  - _Availability_: Mitigating DoS

- **Key Protocols:**

  - **TLS**: Secure handshake/key exchange (`Diffie-Hellman: gᵃ mod p`), versions up to 1.3
  - **IPsec**: AH (integrity), ESP (confidentiality), Transport/Tunnel modes
  - **Others**: SSH (remote), Kerberos (auth)

- **Cryptography:**

  - _Symmetric_: AES (blocks, CBC mode: `Cᵢ=E(K,Pᵢ⊕Cᵢ₋₁)`)
  - _Asymmetric_: RSA (`n=pq`, φ=`(p-1)(q-1)`, public e, private d, `mᵉ mod n`)
  - _Hash_: SHA-256 (collision-resistant)

- **Implementation Tip (Python):**

  ```python
  import ssl
  context = ssl.create_default_context()
  ```

- **Pitfall:** Avoid weak keys; consider post-quantum (e.g. lattice-based) crypto.

- **Example:**  
  _Heartbleed_: OpenSSL flaw that exposed private keys.

---

## AI-Driven Network Optimization

- **Goals:** Minimize latency, maximize throughput

- **AI Techniques:**

  - _Prediction_: LSTM for forecasting traffic
  - _Routing_: Reinforcement Learning (e.g. Q-learning: `Q = r + γ max Q'`)
  - _Load Balancing_: Genetic algorithms

- **Metrics:** Jitter, bandwidth

- **Example:**  
  Huawei 5G slicing reduced network energy use by 20%.

- **Code Example (PyTorch NN):**

  ```python
  import torch.nn as nn
  nn.Linear(1, 1)
  ```

- **Research Direction:**  
  Federated learning for multi-carrier operations

---

## AI-Driven Network Security

- **Methods:**

  - _Anomaly Detection_: Autoencoders (`loss = ∑(x - x′)²`)
  - _Intrusion Detection_: CNNs

- **Tools:**  
  Isolation Forest (`sklearn.ensemble.IsolationForest`)

- **Example:**  
  Google’s AI blocking 99%+ phishing threats.

- **Challenges:**

  - Adversarial ML
  - Ethics, bias in models

- **Tip:**  
  Train/test on public datasets, e.g. CIC-IDS2018.

---

## Quick Formulas & Analogies

- **Network:** Like a postal system (devices = addresses, protocols = rules)
- **Security:** Padlock analogy (public key locks, private unlocks)
- **AI:** Traffic controller (predicts and avoids jams)
- **Project Ideas:**
  - Simulate an RSA breach
  - Build an AI anomaly detector

---
