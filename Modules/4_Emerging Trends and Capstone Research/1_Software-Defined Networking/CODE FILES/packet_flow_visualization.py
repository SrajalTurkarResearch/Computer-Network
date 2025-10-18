# packet_flow_visualization.py
# Plots mock packet flow data to show SDN switch dynamics.
# Purpose: Teach beginners how to visualize network performance.
# Requirements: Install NumPy and Matplotlib (`pip install numpy matplotlib`).
# Usage: Run directly (`python packet_flow_visualization.py`) to display a plot.

import numpy as np
import matplotlib.pyplot as plt

# Mock packet counts over time (simulating an SDN switch)
time = np.arange(0, 10, 1)
packets = [100, 120, 150, 130, 200, 180, 220, 210, 190, 230]

# Plot
plt.figure(figsize=(8, 4))
plt.plot(time, packets, marker="o", color="blue")
plt.xlabel("Time (seconds)")
plt.ylabel("Packets Processed")
plt.title("Packet Flow in SDN Switch")
plt.grid(True)
plt.show()

# Notes for scientists:
# - In real SDN, collect packet counts via OpenFlow counters.
# - Research idea: Plot real-time flows using Ryu and Wireshark data.
