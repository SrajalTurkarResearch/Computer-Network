# shannon_capacity.py: Exploring Shannon’s Capacity in the Physical Layer
# Author: Grok, inspired by Turing, Einstein, Tesla
# Purpose: Tutorial on channel capacity for aspiring scientists

import numpy as np
import matplotlib.pyplot as plt

# --- Theory Summary ---
# Claude Shannon’s theorem defines the maximum error-free data rate (C, in bps).
# Formula: C = B log2(1 + SNR)
# - B: Bandwidth (Hz)
# - SNR: Signal-to-Noise Ratio (linear, convert from dB: SNR = 10^(SNR_dB/10))
# Importance: Sets the theoretical limit for communication systems (e.g., Wi-Fi, 5G).
# Research: Approaching Shannon’s limit drives innovations in coding and modulation.


# --- Shannon Capacity Function ---
def shannon_capacity(B, SNR_dB):
    """Calculate channel capacity given bandwidth and SNR in dB."""
    SNR = 10 ** (SNR_dB / 10)  # Convert dB to linear
    return B * np.log2(1 + SNR)


# Example Calculation
B = 1e6  # 1 MHz
SNR_dB = 20  # 20 dB
C = shannon_capacity(B, SNR_dB)
print(f"Capacity for B={B/1e6} MHz, SNR={SNR_dB} dB: {C/1e6:.2f} Mbps")

# --- Visualization: Capacity vs. SNR ---
SNR_dB_range = np.arange(0, 41, 1)
C_values = [shannon_capacity(B, snr) / B for snr in SNR_dB_range]
plt.figure(figsize=(10, 4))
plt.plot(SNR_dB_range, C_values)
plt.title("Shannon Capacity per Unit Bandwidth vs. SNR")
plt.xlabel("SNR (dB)")
plt.ylabel("Capacity (bits/s/Hz)")
plt.grid(True)
plt.show()

# --- Visualization: Effect of Bandwidth ---
B_values = [1e6, 5e6, 10e6]  # 1, 5, 10 MHz
plt.figure(figsize=(10, 4))
for B in B_values:
    C_vals = [shannon_capacity(B, snr) / 1e6 for snr in SNR_dB_range]
    plt.plot(SNR_dB_range, C_vals, label=f"B={B/1e6} MHz")
plt.title("Capacity vs. SNR for Different Bandwidths")
plt.xlabel("SNR (dB)")
plt.ylabel("Capacity (Mbps)")
plt.legend()
plt.grid(True)
plt.show()

# --- Exercises ---
# 1. Compute C for B=5 MHz, SNR=25 dB.
# 2. Plot capacity for B=2 MHz over SNR=0 to 50 dB.
# 3. Research: How does fading affect capacity in wireless channels?

# --- Research Notes ---
# - Shannon’s limit assumes AWGN; real channels (e.g., fading) use ergodic capacity.
# - Research areas: MIMO systems, quantum channels, AI-optimized coding.
# - Explore polar codes for approaching capacity in 6G.

# Solution to Exercise 1
C_ex = shannon_capacity(5e6, 25)
print(f"Exercise 1 Capacity: {C_ex/1e6:.2f} Mbps")
