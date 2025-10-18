# modulation_techniques.py: Implementing Modulation in the Physical Layer
# Author: Grok, inspired by Turing, Einstein, Tesla
# Purpose: Tutorial on modulation techniques for aspiring scientists

import numpy as np
import matplotlib.pyplot as plt

# --- Theory Summary ---
# Modulation alters a carrier signal to encode data for transmission.
# Types:
# - Analog: AM (amplitude), FM (frequency), PM (phase).
# - Digital: ASK, FSK, PSK, QAM.
# Why Modulate? Enables long-distance transmission, multiplexing, noise resistance.
# Research: Advanced modulation (e.g., 256-QAM) is key for 5G, satellite comm.

# --- AM Modulation ---
t = np.linspace(0, 0.1, 1000)
fc = 100  # Carrier frequency (Hz)
fm = 10  # Message frequency (Hz)
message = np.sin(2 * np.pi * fm * t)
carrier = np.sin(2 * np.pi * fc * t)
am_signal = (1 + 0.5 * message) * carrier  # Modulation index = 0.5

plt.figure(figsize=(10, 4))
plt.plot(t, am_signal, label="AM Signal")
plt.plot(t, message, "r--", label="Message", alpha=0.5)
plt.title("Amplitude Modulation")
plt.xlabel("Time (s)")
plt.ylabel("Amplitude")
plt.legend()
plt.grid(True)
plt.show()

# --- FM Modulation ---
kf = 50  # Frequency deviation
fm_signal = np.sin(2 * np.pi * fc * t + kf * np.cumsum(message) * (t[1] - t[0]))
plt.figure(figsize=(10, 4))
plt.plot(t, fm_signal, label="FM Signal")
plt.title("Frequency Modulation")
plt.xlabel("Time (s)")
plt.ylabel("Amplitude")
plt.legend()
plt.grid(True)
plt.show()

# --- QAM Constellation (16-QAM) ---
I = np.repeat(np.arange(-3, 4, 2), 4)
Q = np.tile(np.arange(-3, 4, 2), 4)
bits = [format(i, "04b") for i in range(16)]  # 4-bit symbols
plt.figure(figsize=(6, 6))
plt.scatter(I, Q)
for i, txt in enumerate(bits):
    plt.annotate(txt, (I[i], Q[i]))
plt.title("16-QAM Constellation Diagram")
plt.xlabel("In-Phase")
plt.ylabel("Quadrature")
plt.grid(True)
plt.show()

# --- Exercises ---
# 1. Implement BPSK for bits [1, 0, 1, 1].
# 2. Calculate bits per symbol for 64-QAM.
# 3. Research: How does OFDM improve Wi-Fi efficiency?

# --- Research Notes ---
# - QAM increases data rate but is noise-sensitive (needs high SNR).
# - OFDM (used in Wi-Fi) splits bandwidth into subcarriers.
# - Explore non-orthogonal multiple access (NOMA) for 6G.

# Solution to Exercise 2
bits_per_symbol = np.log2(64)
print(f"Exercise 2: Bits per symbol for 64-QAM: {bits_per_symbol}")
