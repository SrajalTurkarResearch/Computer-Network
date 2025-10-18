# shannon_capacity.py
# Computes and plots Shannon's channel capacity for varying SNR.
# Demonstrates basic network theory math.

import numpy as np
import matplotlib.pyplot as plt

# Parameters
B = 100e6  # Bandwidth in Hz (100 MHz)
SNR_dB = np.linspace(0, 30, 100)  # SNR range in dB
SNR = 10 ** (SNR_dB / 10)  # Convert to linear scale
C = B * np.log2(1 + SNR)  # Capacity in bps

# Plot
plt.plot(SNR_dB, C / 1e9)  # Convert to Gbps
plt.xlabel("SNR (dB)")
plt.ylabel("Capacity (Gbps)")
plt.title("Shannon Channel Capacity")
plt.grid(True)
plt.show()

print(
    "Plot displayed. Example: At 30 dB SNR, capacity ≈ {:.2f} Gbps".format(C[-1] / 1e9)
)
