```python
# edge_latency_optimization.py
# Purpose: Simulate IoT network load and optimize edge vs. cloud processing for latency.
# Context: IoT systems must balance edge (low latency) and cloud (high capacity) processing.
# This script simulates network load for increasing devices and optimizes edge processing fraction.
# Requirements: numpy, matplotlib

import numpy as np
import matplotlib.pyplot as plt

# Simulate network load
def network_load(devices, data_rate=1000):
    """Calculate total network load in bits/s.
    Args:
        devices (int): Number of devices.
        data_rate (int): Data rate per device in bits/s.
    Returns:
        float: Total load in bits/s.
    """
    return devices * data_rate

# Optimize edge vs. cloud latency
def effective_latency(f_edge, L_edge=1.1, L_cloud=6.1):
    """Calculate effective latency with edge processing fraction.
    Args:
        f_edge (float): Fraction of tasks processed at edge (0 to 1).
        L_edge (float): Edge latency in ms.
        L_cloud (float): Cloud latency in ms.
    Returns:
        float: Effective latency in ms.
    """
    return f_edge * L_edge + (1 - f_edge) * L_cloud

# Simulate network load
device_counts = [100, 500, 1000, 5000]
loads = [network_load(d) / 1e6 for d in device_counts]  # Convert to Mbps

plt.figure(figsize=(8, 5))
plt.plot(device_counts, loads, 'r-s', label='Network Load')
plt.xlabel('Number of Devices')
plt.ylabel('Load (Mbps)')
plt.title('Network Load vs. Device Count')
plt.legend()
plt.grid(True)
plt.show()

# Optimize edge fraction
f_edge_values = np.linspace(0, 1, 100)
latencies = [effective_latency(f) for f in f_edge_values]

plt.figure(figsize=(8, 5))
plt.plot(f_edge_values, latencies, 'g-', label='Effective Latency')
plt.xlabel('Edge Processing Fraction')
plt.ylabel('Latency (ms)')
plt.title('Optimizing Edge vs. Cloud Processing')
plt.legend()
plt.grid(True)
plt.show()
```