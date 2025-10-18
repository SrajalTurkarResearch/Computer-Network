# security_ddos_detection.py
# Detects potential DDoS attacks in SDN using entropy-based analysis.
# Purpose: Demonstrate SDN's security capabilities, inspired by 2023 hospital attack mitigation.
# Requirements: Install NumPy (`pip install numpy`).
# Usage: Run directly (`python security_ddos_detection.py`) to compute entropy.

import numpy as np

# Mock packet counts from source IPs
packets_normal = [50, 30, 20]  # Normal traffic: diverse sources
packets_attack = [90, 10]  # Attack traffic: mostly one source


def compute_entropy(packets):
    """Compute entropy of packet distribution."""
    total = sum(packets)
    probs = [p / total for p in packets]
    H = -sum(p * np.log2(p) for p in probs if p > 0)
    return H


# Compute and compare entropy
H_normal = compute_entropy(packets_normal)
H_attack = compute_entropy(packets_attack)
print(f"Normal traffic entropy: {H_normal:.2f} (Expected: ~1.5)")
print(f"Attack traffic entropy: {H_attack:.2f} (Expected: <0.5)")
print("Alert: DDoS detected!" if H_attack < 0.5 else "No attack detected.")

# Notes for scientists:
# - Real-world impact: SDN blocked a hospital ransomware attack in 2023.
# - Research idea: Integrate with Ryu to block low-entropy IPs dynamically.
# - Try in Mininet: Simulate traffic with `iperf` and log packet counts.
