```python
# smart_agriculture_project.py
# Purpose: Simulate an IoT network of soil moisture sensors in a farm with edge computing.
# Context: In smart agriculture (e.g., John Deere), IoT sensors monitor soil moisture, and edge nodes
# process data locally to adjust irrigation, saving 20-30% water. This project models device scalability
# and latency reduction using edge vs. cloud processing.
# Requirements: numpy, matplotlib
# Scalability: Handles increasing sensor counts.
# Latency: Compares edge vs. cloud for irrigation decisions.

import numpy as np
import matplotlib.pyplot as plt

def sensor_network_load(sensors, data_rate=500):
    """Calculate network load for soil moisture sensors.
    Args:
        sensors (int): Number of sensors.
        data_rate (float): Data rate per sensor in bits/s.
    Returns:
        float: Total network load in Mbps.
    """
    return sensors * data_rate / 1e6  # Convert to Mbps

def irrigation_latency(distance, speed=200, packet_size=4000, bandwidth=10e6, queue=0.1, proc=0.05):
    """Calculate latency for irrigation decision.
    Args:
        distance (float): Distance to server in km.
        speed (float): Signal speed in km/ms (approx. 200 km/ms in fiber).
        packet_size (int): Data size in bits (small for sensors).
        bandwidth (float): Network speed in bits/s (e.g., 10 Mbps for rural).
        queue (float): Queuing delay in ms.
        proc (float): Processing delay in ms.
    Returns:
        float: Total latency in ms.
    """
    D_p = distance / speed  # Propagation delay
    D_t = packet_size / bandwidth * 1000  # Transmission delay (s to ms)
    return D_p + D_t + queue + proc

# Simulate scalability: Network load for increasing sensors
sensor_counts = [100, 500, 1000, 2000, 5000]
loads = [sensor_network_load(s) for s in sensor_counts]

# Simulate latency: Edge (1 km) vs. Cloud (1000 km)
edge_latency = irrigation_latency(1)  # Local edge node
cloud_latency = irrigation_latency(1000)  # Remote cloud server
print(f"Smart Agriculture - Edge Latency: {edge_latency:.2f} ms, Cloud Latency: {cloud_latency:.2f} ms")

# Visualize network load
plt.figure(figsize=(8, 5))
plt.plot(sensor_counts, loads, 'b-s', label='Network Load')
plt.xlabel('Number of Sensors')
plt.ylabel('Load (Mbps)')
plt.title('Scalability: Network Load in Smart Agriculture')
plt.legend()
plt.grid(True)
plt.show()

# Visualize latency comparison
categories = ['Edge (1 km)', 'Cloud (1000 km)']
latencies = [edge_latency, cloud_latency]
plt.figure(figsize=(6, 4))
plt.bar(categories, latencies, color=['green', 'red'])
plt.ylabel('Latency (ms)')
plt.title('Latency: Edge vs. Cloud in Irrigation Decisions')
plt.show()

# Research Extension: Modify sensor_counts or data_rate to test scalability limits.
# Add queuing delay model (M/M/1) for more realism.
# Investigate low-power protocols like NB-IoT for rural areas.
```