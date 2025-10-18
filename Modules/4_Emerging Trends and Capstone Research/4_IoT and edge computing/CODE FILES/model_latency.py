```python
# model_latency.py
# Purpose: Calculate and compare latency for edge vs. cloud in IoT networks.
# Context: Latency is the total delay (propagation, transmission, queuing, processing).
# Edge computing reduces latency by processing near devices. This script computes
# latency for a 1 km (edge) vs. 1000 km (cloud) link and visualizes components.
# Requirements: numpy, matplotlib

import numpy as np
import matplotlib.pyplot as plt

def calculate_latency(distance, speed=200, packet_size=80000, bandwidth=100e6, queue=0.2, proc=0.1):
    """Calculate total latency in milliseconds.
    Args:
        distance (float): Distance to server in km.
        speed (float): Signal speed in km/ms (approx. 200 km/ms in fiber).
        packet_size (int): Data size in bits.
        bandwidth (float): Network speed in bits/s.
        queue (float): Queuing delay in ms.
        proc (float): Processing delay in ms.
    Returns:
        float: Total latency in ms.
    """
    D_p = distance / speed  # Propagation delay (ms)
    D_t = packet_size / bandwidth * 1000  # Transmission delay (s to ms)
    return D_p + D_t + queue + proc

# Calculate latencies
edge_latency = calculate_latency(1)  # 1 km for edge
cloud_latency = calculate_latency(1000)  # 1000 km for cloud
print(f"Edge Latency: {edge_latency:.2f} ms, Cloud Latency: {cloud_latency:.2f} ms")

# Visualize latency components
components = ['Propagation', 'Transmission', 'Queuing', 'Processing']
edge_values = [0.005, 0.8, 0.2, 0.1]  # For 1 km
cloud_values = [5.0, 0.8, 0.2, 0.1]  # For 1000 km

x = np.arange(len(components))
width = 0.35

fig, ax = plt.subplots(figsize=(10, 6))
ax.bar(x - width/2, edge_values, width, label='Edge (1 km)')
ax.bar(x + width/2, cloud_values, width, label='Cloud (1000 km)')
ax.set_xlabel('Latency Components')
ax.set_ylabel('Time (ms)')
ax.set_title('Latency Breakdown: Edge vs. Cloud')
ax.set_xticks(x)
ax.set_xticklabels(components)
ax.legend()
plt.show()
```