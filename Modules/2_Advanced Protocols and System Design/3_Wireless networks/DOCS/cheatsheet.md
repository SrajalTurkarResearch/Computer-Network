# Wireless Networks Cheatsheet

A concise reference for the Jupyter Notebook tutorial on IEEE 802.11, channel access, and 5G. Perfect for researchers and aspiring scientists. Keep this handy for quick review or notebook integration.

## 1. Computer Networks Basics

- **Definition** : Connect devices to share data via packets (like notes with addresses).
- **Components** : Nodes (devices), links (wired/wireless), protocols (TCP/IP), routers/switches.
- **Types** : LAN (home Wi-Fi), WAN (internet), PAN (Bluetooth).
- **Analogy** : Playground where kids pass notes, guided by rules.
- **Key Formula** : Shannon’s Capacity: **C = B \* log₂(1 + SNR)**
- Ex: B=20 MHz, SNR=15 → C=20e6 \* log₂(16)=80 Mbps.
- **Notebook Tip** : Sketch devices → router with packet arrows.

## 2. OSI Model

- **Layers** : 7 steps for data transfer; wireless focuses on:
- Layer 1 (Physical): Bits over waves.
- Layer 2 (Data Link): Frames, MAC addresses, access control.
- **Analogy** : Pizza-making: Layer 1 (ingredients), Layer 2 (dough+toppings).
- **Tool** : Wireshark to see frames (Layer 2).
- **Notebook Tip** : Draw 7-layer stack, highlight 1–2.

## 3. Wireless Physics

- **Signals** : Radio waves (2.4 GHz, 5 GHz, mmWave).
- **Challenges** : Path loss, fading, interference.
- **Key Formula** : Friis Equation: **Pr = Pt _ Gt _ Gr \* (λ / (4πd))²**
- Ex: Pt=0.1 W, Gt=Gr=2, λ=0.125 m, d=100 m → Pr≈4e-9 W.
- **Modulation** : ASK, FSK, QAM, OFDM.
- QAM: η = log₂(M). Ex: 64-QAM → log₂(64)=6 bits/symbol.
- **Notebook Tip** : Sketch antennas with direct/bounced signals; note Friis calc.

## 4. 802.11 Standards (Wi-Fi)

- **Evolution** :
- 802.11b: 2.4 GHz, 11 Mbps.
- 802.11n (Wi-Fi 4): 600 Mbps, MIMO.
- 802.11ax (Wi-Fi 6): 9.6 Gbps, OFDMA.
- Wi-Fi 7: 46 Gbps, Multi-Link Operation.
- **Rate Formula** : **Rate = B _ log₂(M) _ N \* R**
- Ex: B=80 MHz, 256-QAM (log₂=8), N=2, R=5/6 → 1.07 Gbps.
- **Features** : MU-MIMO, OFDMA, TWT, WPA3 security.
- **Notebook Tip** : Draw Wi-Fi family tree (b→ax); list one feature.

## 5. Channel Access Models

- **CSMA/CA** : Listen, backoff, send (Wi-Fi).
- Collision prob: p ≈ 1/(CW+1). Ex: CW=15, n=10 → p≈0.47.
- Throughput: η ≈ T_data / (T_data + T_backoff + T_collision).
- **Others** : OFDMA (Wi-Fi 6, 5G), TDMA (cellular).
- **Analogy** : Classroom rules for taking turns.
- **Notebook Tip** : Draw CSMA/CA flowchart; note p formula.

## 6. 5G Architecture

- **Components** : RAN (gNBs, Massive MIMO), Core (AMF, SMF, UPF), slicing.
- **Features** : Low latency (1 ms), V2X, edge computing.
- **Rate Formula** : **C = B _ log₂(1 + SNR) _ min(Nt, Nr)**
- Ex: B=100 MHz, SNR=100, Nt=64, Nr=4 → 2.66 Gbps.
- **Analogy** : RAN = mail carriers, Core = post office, slicing = custom delivery.
- **Notebook Tip** : Sketch phone → gNB → Core; note latency calc.

## 7. Tools for Research

- **NS-3** : Simulate Wi-Fi/5G networks.
- **Wireshark** : Capture packets (beacons, data).
- **Python** : NumPy (math), Matplotlib (plots), Scapy (packets).
- **Notebook Tip** : List one tool and its use (e.g., NS-3 for throughput).

## 8. Key Python Scripts

- `shannon_capacity.py`: Compute C = B \* log₂(1 + SNR).
- `friis_path_loss.py`: Plot Pr vs. distance.
- `csma_ca_collision.py`: Simulate collision probability.
- `mimo_throughput.py`: Calculate 5G MIMO rate.
- `traffic_analysis.py`: Plot 5G traffic (needs dataset).
- **Notebook Tip** : Run one script; note its output.

## 9. Research Ideas

- **Wi-Fi** : Optimize OFDMA for 100 IoT devices (use `csma_ca_collision.py`).
- **5G** : Slicing for telescope data; model latency.
- **6G** : Terahertz or quantum-resistant security.
- **Notebook Tip** : Pick one idea, sketch a simulation plan.

## 10. Exercises

1. Calculate Shannon: B=40 MHz, SNR=31 → 200 Mbps.
2. Friis at 5 GHz: λ=3e8/5e9=0.06 m, solve Pr.
3. Simulate CSMA/CA: Vary n in `csma_ca_collision.py`.

- **Notebook Tip** : Work through one exercise; verify with code.

## 11. What’s Missing in Standard Tutorials

- Deep math (e.g., Friis derivation: 1/d² from spherical spreading).
- Rare insights: Wi-Fi for gesture recognition via CSI.
- ML integration: Predict network failures with traffic data.
- **Notebook Tip** : Note one missing topic for your research.

  **Quick Tips** :

- **Visualize** : Draw OSI stack, Wi-Fi tree, 5G architecture.
- **Experiment** : Modify Python parameters (e.g., SNR, CW).
- **Connect** : Link each concept to a case study (e.g., 5G latency → telemedicine).
