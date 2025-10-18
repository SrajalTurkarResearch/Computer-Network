# friis_path_loss.py
# Simulates Friis Path Loss for wireless signal strength vs. distance
# Purpose: Visualize how received power decreases with distance
# Math: Pr = Pt * Gt * Gr * (λ / (4πd))^2, where Pr is received power, Pt is transmit power,
#       Gt/Gr are antenna gains, λ is wavelength, d is distance
# Usage: Run to plot received power (dBm) vs. distance

import numpy as np
import matplotlib.pyplot as plt


def calculate_friis_power(Pt, Gt, Gr, f, d):
    """
    Calculate received power using Friis equation
    Parameters:
        Pt (float): Transmit power (W)
        Gt, Gr (float): Transmit and receive antenna gains
        f (float): Frequency (Hz)
        d (numpy array): Distance (m)
    Returns:
        numpy array: Received power (W)
    """
    c = 3e8  # Speed of light (m/s)
    lambda_wave = c / f  # Wavelength = c/f
    # Friis equation: Pr = Pt * Gt * Gr * (λ / (4πd))^2
    Pr = Pt * Gt * Gr * (lambda_wave / (4 * np.pi * d)) ** 2
    return Pr


# Parameters
Pt = 0.1  # Transmit power: 100 mW
Gt = Gr = 2  # Antenna gains
f = 2.4e9  # Frequency: 2.4 GHz
d = np.logspace(0, 3, 100)  # Distances from 1 to 1000 m (log scale)

# Calculate received power
Pr = calculate_friis_power(Pt, Gt, Gr, f, d)

# Convert to dBm for plotting
Pr_dBm = 10 * np.log10(Pr * 1000)  # Convert W to mW, then to dBm

# Plot
plt.figure(figsize=(8, 6))
plt.plot(d, Pr_dBm)
plt.xlabel("Distance (m)")
plt.ylabel("Received Power (dBm)")
plt.title("Friis Path Loss at 2.4 GHz")
plt.grid(True)
plt.xscale("log")
plt.show()
# Expected: Power drops quadratically with distance (~-80 dBm at 100 m)
