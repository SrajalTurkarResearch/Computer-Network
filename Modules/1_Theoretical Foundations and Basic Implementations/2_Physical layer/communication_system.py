# communication_system.py: Simulating a Full Communication System
# Author: Grok, inspired by Turing, Einstein, Tesla
# Purpose: Major project for aspiring scientists to simulate a communication system

import numpy as np
import matplotlib.pyplot as plt

# --- Theory Summary ---
# A communication system involves:
# 1. Data generation (bits).
# 2. Modulation (e.g., BPSK).
# 3. Channel (add noise).
# 4. Demodulation.
# 5. Error analysis (Bit Error Rate, BER).
# Research: Optimizing systems to approach Shannon’s limit is key for 5G, IoT.

# --- Generate Random Bits ---
np.random.seed(42)
bits = np.random.randint(0, 2, 1000)  # 1000 bits

# --- BPSK Modulation ---
# Map 1 -> +1, 0 -> -1
symbols = 2 * bits - 1

# --- Channel: Add AWGN ---
SNR_dB = 10
noise_var = 1 / (10 ** (SNR_dB / 10))
noise = np.sqrt(noise_var) * np.random.randn(len(symbols))
received = symbols + noise

# --- Demodulation ---
decoded = (received > 0).astype(int)

# --- Bit Error Rate (BER) ---
ber = np.mean(bits != decoded)
print(f"Bit Error Rate: {ber:.4f}")

# --- Visualization: Transmitted vs. Received ---
plt.figure(figsize=(10, 4))
plt.scatter(range(50), symbols[:50], label="Transmitted Symbols", marker="o")
plt.scatter(range(50), received[:50], label="Received Symbols", marker="x", alpha=0.7)
plt.title("BPSK Symbols Before and After Channel")
plt.xlabel("Symbol Index")
plt.ylabel("Amplitude")
plt.legend()
plt.grid(True)
plt.show()

# --- BER vs. SNR Analysis ---
SNR_dB_range = np.arange(0, 21, 2)
ber_values = []
for snr in SNR_dB_range:
    noise_var = 1 / (10 ** (snr / 10))
    noise = np.sqrt(noise_var) * np.random.randn(len(symbols))
    received = symbols + noise
    decoded = (received > 0).astype(int)
    ber_values.append(np.mean(bits != decoded))
plt.figure(figsize=(10, 4))
plt.semilogy(SNR_dB_range, ber_values)
plt.title("BER vs. SNR for BPSK")
plt.xlabel("SNR (dB)")
plt.ylabel("Bit Error Rate")
plt.grid(True)
plt.show()

# --- Exercises ---
# 1. Implement QPSK modulation (2 bits per symbol).
# 2. Compute BER for SNR=15 dB.
# 3. Research: How do error-correcting codes reduce BER?

# --- Research Notes ---
# - BPSK is robust but low-rate; QAM increases throughput.
# - Turbo/LDPC codes approach Shannon’s limit.
# - Explore AI-driven channel estimation for fading channels.

# Solution to Exercise 2
noise_var_ex = 1 / (10 ** (15 / 10))
noise_ex = np.sqrt(noise_var_ex) * np.random.randn(len(symbols))
received_ex = symbols + noise_ex
decoded_ex = (received_ex > 0).astype(int)
ber_ex = np.mean(bits != decoded_ex)
print(f"Exercise 2 BER for SNR=15 dB: {ber_ex:.4f}")
