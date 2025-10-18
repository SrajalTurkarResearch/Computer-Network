# Data Link Layer Cheat Sheet

A concise reference for the Data Link Layer (Layer 2, OSI model), focusing on MAC protocols and error detection/correction. Designed for researchers and aspiring scientists to quickly grasp key concepts, formulas, and research insights. Use with `Data_Link_Layer_Guide.ipynb` and Python files (`pure_aloha_simulation.py`, `crc_error_detection.py`, `hamming_code.py`). Date: September 09, 2025.

## 1. Core Concepts

- **Role** : Ensures reliable local data transfer over noisy, shared Layer 1 media (wires, radio).
- **Functions** :
- **Framing** : Wraps data into frames ([Header | Data | Trailer]). Bit stuffing: Insert 0 after five 1s to avoid flag (01111110).
- **Physical Addressing** : 48-bit MAC addresses (e.g., 00:1A:2B:3C:4D:5E). Unicast, broadcast (FF:FF:…), multicast.
- **Flow Control** : Sliding window (send W frames, wait ACK). Utilization: U = min(1, W/(1+2a)), a = propagation delay / frame time.
- **Error Control** : Detect (Parity, CRC) or correct (Hamming, Reed-Solomon).
- **Access Control** : MAC protocols manage shared media.

  **Visualization** : Sketch OSI stack:

```
L7: Application | L6: Presentation | L5: Session | L4: Transport | L3: Network | L2: Data Link | L1: Physical
```

## 2. MAC Protocols: Key Formulas & Mechanics

- **Pure ALOHA** :
- **How** : Send anytime; collision if overlap within 2T (T=frame time).
- **Formula** : S = G \* e^(-2G), max 0.184 at G=0.5 (Poisson-derived).
- **Use** : Simple IoT (e.g., ocean buoys).
- **Slotted ALOHA** :
- **How** : Send at slot start (sync clocks).
- **Formula** : S = G \* e^(-G), max 0.368 at G=1.
- **Use** : RFID, satellite links.
- **CSMA/CD (Ethernet)** :
- **How** : Listen, send, detect collision, jam, backoff (0 to 2^k-1 slots, k≤10).
- **Use** : Wired data centers (e.g., CERN).
- **CSMA/CA (WiFi)** :
- **How** : Listen, RTS/CTS, backoff. NAV timer avoids hidden terminals.
- **Use** : Wireless (e.g., hospital devices).
- **Advanced** :
- TDMA: Fixed slots, S~1. Use: 4G, telescope arrays.
- TRMAC (2025): Time-reversal for HPC, S>0.9.

  **Visualization** : Sketch ALOHA collision:

```
Time: 0---1---2
A: [Frame]   [Retry]
B:   [Frame][Retry]
Collision: ^^
```

## 3. Error Detection & Correction

- **Parity** :
- **How** : Add bit for even/odd 1s count. Detects odd-bit errors.
- **Limit** : Misses even errors.
- **Checksum** :
- **How** : Sum bytes, append one’s complement. Detects most errors.
- **Limit** : Weak for bursts.
- **CRC** :
- **How** : Divide data polynomial by generator (e.g., 1011 = x^3 + x + 1). Append remainder.
- **Formula** : Detects bursts ≤ deg(generator). E.g., CRC-32 HD=6.
- **Use** : Ethernet, Mars rovers.
- **Example** : Data 110101 ÷ 1011 → remainder 001.
- **Hamming Code** :
- **How** : Parity bits at 2^i (1,2,4,…). Syndrome = error position.
- **Formula** : For m data bits, r parity: 2^r ≥ m+r+1. Corrects 1 error (d=3).
- **Example** : Data 1011 → [0,1,1,0,0,1,1]. Error at pos 5 → syndrome 101 (5).
- **Use** : ECC memory, quantum networks.
- **Advanced** :
- Reed-Solomon: Corrects bursts (e.g., RS(255,223) → 16 errors).
- PBEDC (2025): Perturbation-based for nano-networks.

  **Visualization** : Hamming positions:

```
Pos: 1(p1) 2(p2) 3(d1) 4(p4) 5(d2) 6(d3) 7(d4)
p1:  x     x     x     x
p2:     x  x     x     x
p4:           x  x  x  x
```

## 4. Key Algorithms (Pseudo-Code)

- **Pure ALOHA** :

```
  while True:
      if data_to_send:
          send_frame()
          wait_for_ack(timeout)
          if no_ack: backoff(random)
```

- **CRC** :

```
  extend data with (deg(generator)-1) zeros
  for i in range(len(data)):
      if data[i] == 1:
          XOR data[i:i+len(generator)] with generator
  return remainder
```

- **Hamming Encode** :

```
  find r: 2^r ≥ m+r+1
  place data at non-2^i positions
  for i in 0 to r-1:
      parity[i] = XOR of bits where pos has 1 in bit i
```

## 5. Research Insights

- **MAC** : AI-driven MAC for 6G (adapts to traffic via ML).
- **Error Control** : Quantum multimode codes reduce qubit overhead (Quantinuum 2025).
- **Rare Insight** : TRMAC uses time-reversal physics (like Einstein’s relativity) for ultra-low latency.
- **Ethical Note** : Fair MAC protocols critical for equitable access in resource-scarce regions.

## 6. Quick Reference Table

| Protocol/Code | Use Case | Key Metric | Limitation      |
| ------------- | -------- | ---------- | --------------- |
| Pure ALOHA    | IoT      | S=0.184    | High collisions |
| Slotted ALOHA | RFID     | S=0.368    | Needs sync      |
| CSMA/CA       | WiFi     | S~0.7      | Overhead        |
| CRC           | Ethernet | HD=6       | Detection only  |
| Hamming       | ECC      | Correct 1  | Single error    |

## 7. Research Directions

- **Simulate** : Use `pure_aloha_simulation.py` to test new MACs.
- **Extend** : Modify `hamming_code.py` for BCH codes.
- **Innovate** : Design AI-MAC for 6G or quantum FEC for noisy channels.
- **Read** : IEEE 802.3/802.11, Hamming’s 1950 paper, TRMAC (2025).

## 8. What’s Missing in Standard Tutorials

- Derivations (e.g., S = G \* e^(-2G) from Poisson).
- Quantum parallels: Hamming → stabilizer codes.
- 2025 advances: TRMAC, PBEDC for nano-nets.
- Ethical MAC design for fairness.

  **Notebook Note** : Sketch visualizations, run Python files, question “why” like Turing, derive like Einstein, build like Tesla.
