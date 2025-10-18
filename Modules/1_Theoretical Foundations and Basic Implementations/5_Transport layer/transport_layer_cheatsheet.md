# Transport Layer Cheat Sheet

A quick reference for TCP/UDP mechanics, flow control, and congestion control. Perfect for your scientist’s notebook!

## 1. Transport Layer Basics

- **Role** : Delivers data between apps on different devices (OSI Layer 4).
- **Protocols** : TCP (reliable, like insured mail), UDP (fast, like postcards).
- **Key Jobs** :
- **Ports** : App addresses (e.g., 80 for HTTP).
- **Segmentation** : Splits data into packets.
- **Delivery** : TCP ensures order; UDP prioritizes speed.
- **Analogy** : Librarian sorting books for readers via delivery trucks (IP).
- **Example** : TCP for file downloads, UDP for video calls.
- **Research Tip** : Study ports in IoT networks; simulate with `socket` in Python.

## 2. UDP Mechanics

- **How It Works** : Sends datagrams (data + 8-byte header: ports, length, checksum). No connection, no retransmits.
- **Key Terms** :
- **Datagram** : Standalone packet (max 64KB).
- **Checksum** : Error check (sum of bits, flipped).
- **Port** : 0-65535 (e.g., 53 for DNS).
- **Analogy** : Sending texts—quick, but no delivery confirmation.
- **Example** : Live gaming (UDP for speed).
- **Math** : Efficiency = data/(data+8). Loss probability (p) reduces throughput: (1-p) \* efficiency.
- **Visual** :

```
  [Src Port | Dst Port | Length | Checksum | Data]
```

- **Research Tip** : Test UDP loss rates in ns-3; explore QUIC (UDP-based reliability).

## 3. TCP Mechanics

- **How It Works** :

1. **Handshake** : SYN (ISS), SYN-ACK (IRS), ACK.
2. **Data** : Segments with SEQ/ACK; retransmit if lost (RTO).
3. **Close** : FIN, ACK, FIN, ACK; TIME-WAIT (4 min).

- **Key Terms** :
- **SYN** : Start flag, sets ISS (random sequence number).
- **ACK** : Confirms bytes (next expected SEQ).
- **SEQ** : Byte number for order (32-bit).
- **FIN** : End flag.
- **ISS/IRS** : Initial send/receive sequence numbers.
- **MSS** : Max segment size (~1460 bytes).
- **RTO** : Retransmit timeout (RTT + 4\*variance).
- **Checksum** : Error check.
- **URG/PUSH** : Urgent data; instant delivery.
- **SACK** : Selective ACK for multiple losses.
- **Analogy** : Mailing a numbered book, with receipts.
- **Example** : Banking apps (TCP ensures no errors).
- **Math** : Segments = ceil(data/MSS). RTO = RTT + 4\*RTTVAR.
- **Visual** :

```
  Client --> SYN(100) --> Server
         <-- SYN-ACK(300, ACK=101)
         --> ACK(301)
```

- **Research Tip** : Simulate handshake in Scapy; study SACK in wireless.

## 4. Flow Control

- **How It Works** : Prevents sender from overwhelming receiver using sliding window (rwnd).
- **Key Terms** :
- **Rwnd** : Receiver’s free buffer (advertised in TCP header).
- **Nagle’s Algorithm** : Batches small sends (200ms).
- **Silly Window Syndrome** : Avoids tiny windows.
- **Analogy** : Filling a cup only to its brim.
- **Example** : Slow phone paces server via small rwnd.
- **Math** : Throughput = rwnd/RTT (e.g., 64KB/100ms = 5.12Mbps).
- **Visual** :

```
  Sender: [1-100 sent | 101-200 window]
  Receiver: rwnd=100 bytes
```

- **Research Tip** : Test buffer sizes in IoT; analyze bufferbloat.

## 5. Congestion Control

- **How It Works** : Avoids network jams via cwnd adjustments.
- **Algorithms** :
- **Slow Start** : Doubles cwnd per RTT until ssthresh.
- **Congestion Avoidance** : Adds ~1 MSS per RTT.
- **Fast Retransmit** : 3 dup ACKs trigger resend.
- **Fast Recovery** : Adjusts cwnd post-loss.
- **AIMD** : +1 MSS/RTT, halve on loss.
- **BBR (2025)** : Matches BDP (BW \* RTT).
- **MSS-TCP** : ML for 5G mmWave.
- **Key Terms** :
- **Cwnd** : Congestion window (unACKed data limit).
- **Ssthresh** : Slow start to avoidance switch.
- **FlightSize** : Sent but unACKed bytes.
- **Dup ACK** : Signals loss.
- **ECN** : Router warns of congestion.
- **Analogy** : Driving—speed up slowly, brake for traffic.
- **Example** : Zoom’s TCP scaled during 2020 surges.
- **Math** : AIMD equilibrium: cwnd ≈ sqrt(1.5/p) \* MSS/RTT.
- **Visual** :

```
  Cwnd: 1 -> 2 -> 4 -> 8 -> [Loss] -> 4 -> 5
```

- **Research Tip** : Compare BBR vs. CUBIC in Mininet; explore AI congestion control.

## 6. TCP vs. UDP

| Feature     | TCP        | UDP              |
| ----------- | ---------- | ---------------- |
| Connection  | Yes        | No               |
| Reliability | Yes (ACKs) | No               |
| Order       | Yes (SEQ)  | No               |
| Speed       | Slower     | Faster           |
| Use         | Files, web | Streaming, games |

## 7. Research Hooks

- **Simulate** : TCP handshake, UDP loss in Python (`socket`).
- **Analyze** : Wireshark for SEQ/ACK patterns.
- **Innovate** : QUIC for 6G; quantum-secure TCP.
- **Publish** : BBR in Starlink; MSS-TCP in 5G.

## 8. Missing in Most Tutorials

- Flow-congestion interplay (e.g., rwnd-cwnd mismatch).
- 2025 AI congestion control (20-30% less latency).
- Quantum threats to SEQ numbers.
