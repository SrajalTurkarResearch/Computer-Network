# signal_theory.py: Understanding Signals in the Physical Layer
# Author: Grok, inspired by Turing, Einstein, Tesla
# Purpose: Comprehensive tutorial for aspiring scientists on signal theory

import numpy as np
import matplotlib.pyplot as plt
from scipy.fft import fft, fftfreq

# --- Theory Summary ---
# Signals are physical representations of data (e.g., voltage, light, radio waves).
# Types: Analog (continuous, like voice) vs. Digital (discrete, like bits).
# Key Properties:
# - Amplitude (A): Signal strength.
# - Frequency (f): Cycles per second (Hz).
# - Phase (φ): Wave shift.
# - Bandwidth (B): Frequency range.
# Challenges: Noise (random distortion), Attenuation (signal loss), Interference.
# Research: Signal processing is key in 5G, MRI, and space communication.

# --- Signal Generation ---
# Create a sine wave signal with noise
t = np.linspace(0, 1, 1000)  # Time array (1 second, 1000 points)
f = 5  # Frequency (5 Hz)
A = 3  # Amplitude
signal_clean = A * np.sin(2 * np.pi * f * t)  # s(t) = A sin(2πft)
noise = 0.5 * np.random.randn(len(t))  # Gaussian noise
signal_noisy = signal_clean + noise

# Visualize
plt.figure(figsize=(10, 4))
plt.plot(t, signal_clean, label="Clean Signal (5 Hz)")
plt.plot(t, signal_noisy, label="Noisy Signal", alpha=0.7)
plt.title("Analog Signal with Noise")
plt.xlabel("Time (s)")
plt.ylabel("Amplitude")
plt.legend()
plt.grid(True)
plt.show()

# --- Signal-to-Noise Ratio (SNR) ---
# SNR = 10 log10(P_signal / P_noise), where P = A^2 / 2 for sine waves
P_signal = (A**2) / 2
P_noise = np.var(noise)
SNR_dB = 10 * np.log10(P_signal / P_noise)
print(f"SNR: {SNR_dB:.2f} dB")

# --- Fourier Analysis ---
# Compute frequency spectrum to see signal components
N = len(t)
yf = fft(signal_noisy)
xf = fftfreq(N, t[1] - t[0])[: N // 2]  # Positive frequencies
plt.figure(figsize=(10, 4))
plt.plot(xf, 2.0 / N * np.abs(yf[: N // 2]))
plt.title("Frequency Spectrum of Noisy Signal")
plt.xlabel("Frequency (Hz)")
plt.ylabel("Amplitude")
plt.grid(True)
plt.show()

# --- Digital Signal Example ---
# Generate a binary signal (0s and 1s)
bits = np.array([1, 0, 1, 1, 0])
t_digital = np.linspace(0, len(bits), len(bits) * 100)
digital_signal = np.repeat(bits, 100)  # Stretch bits for visualization
plt.figure(figsize=(10, 4))
plt.step(t_digital, digital_signal, where="post")
plt.title("Digital Signal (Binary Sequence)")
plt.xlabel("Time (s)")
plt.ylabel("Amplitude (0 or 1)")
plt.grid(True)
plt.show()

# --- Exercises ---
# 1. Modify the frequency to 10 Hz and replot the clean signal.
# 2. Calculate SNR for A=5, noise variance=1.
# 3. Research: How does Fourier analysis help in detecting exoplanet signals?

# --- Research Notes ---
# - Fourier transforms decompose signals into frequencies, critical for compression (MP3) and astronomy.
# - Noise modeling (e.g., AWGN) is foundational for error correction in 6G.
# - Explore non-linear signal processing for biological systems (e.g., neural signals).

# Solution to Exercise 2
A_ex = 5
P_signal_ex = (A_ex**2) / 2
P_noise_ex = 1
SNR_ex = 10 * np.log10(P_signal_ex / P_noise_ex)
print(f"Exercise 2 SNR: {SNR_ex:.2f} dB")
