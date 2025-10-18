# entropy_security.py
# Computes entropy to detect potential network attacks in SDN.
# Purpose: Introduce security analysis for SDN research.
# Requirements: Install NumPy (`pip install numpy`).
# Usage: Run directly (`python entropy_security.py`) to compute entropy.

import numpy as np

# Mock packet counts from different source IPs
packets = [50, 30, 20]  # Example: 50 packets from IP1, 30 from IP2, 20 from IP3
total = sum(packets)
probs = [p / total for p in packets]  # Probabilities

# Compute entropy: H = -sum(p_i * log2(p_i))
H = -sum(p * np.log2(p) for p in probs if p > 0)
print(f"Entropy: {H:.2f}")  # Normal: ~1.5, Attack: <0.5

# Notes for scientists:
# - Low entropy (<0.5) suggests an attack (e.g., DDoS from one source).
# - Research idea: Integrate with Ryu to block low-entropy IPs dynamically.
# - Extend by collecting real packet data via OpenFlow.
