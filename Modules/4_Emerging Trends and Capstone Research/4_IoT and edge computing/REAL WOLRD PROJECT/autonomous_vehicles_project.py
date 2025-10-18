```python
# autonomous_vehicles_project.py
# Purpose: Simulate edge computing in an autonomous vehicle for low-latency decisions.
# Context: In autonomous vehicles (e.g., Tesla), edge computing processes sensor data (1 GB/min)
# locally for instant decisions like braking (<10 ms latency). This project models latency for
# edge vs. cloud processing and visualizes the impact.
# Requirements: numpy, matplotlib
# Scalability: Supports multiple sensors per vehicle.
# Latency: Emphasizes edge for real-time safety.

import numpy as np
import matplotlib.pyplot as plt

def vehicle_sensor_latency(distance, speed=200, packet_size=80000, bandwidth=100e6, queue=0.05, proc=0.02):
    """Calculate latency for sensor data processing in a vehicle.
    Args:
        distance (float): Distance to processing unit in km (0 for on-board edge).
        speed (float): Signal speed in km/ms.
        packet_size (int): Data size in bits (e.g., 10 KB for one sensor reading).
        bandwidth (float): Network speed in bits/s (e.g., 100 Mbps for 5G).
        queue (float): Queuing delay in ms.
        proc (float): Processing delay in ms (low for edge GPUs).
    Returns:
        float: Total latency in ms.
    """
    D_p = distance / speed  # Propagation delay
    D_t = packet_size / bandwidth * 1000  # Transmission delay (s to ms)
    return D_p + D_t + queue + proc

# Simulate latency: On-board edge (0 km) vs. Cloud (500 km)
edge_latency = vehicle_sensor_latency(0)  # On-board processing
cloud_latency = vehicle_sensor_latency(500)  # Cloud server
print(f"Autonomous Vehicles - Edge Latency: {edge_latency:.2f} ms, Cloud Latency: {cloud_latency:.2f} ms")

# Simulate multiple sensors' impact on latency
sensor_counts = [1, 5, 10, 20]
edge_latencies = [vehicle_sensor_latency(0, packet_size=80000 * n) for n in sensor_counts]
cloud_latencies = [vehicle_sensor_latency(500, packet_size=80000 * n) for n in sensor_counts]

# Visualize latency for multiple sensors
plt.figure(figsize=(8, 5))
plt.plot(sensor_counts, edge_latencies, 'g-o', label='Edge (On-board)')
plt.plot(sensor_counts, cloud_latencies, 'r-s', label='Cloud (500 km)')
plt.xlabel('Number of Sensors')
plt.ylabel('Latency (ms)')
plt.title('Latency: Edge vs. Cloud with Multiple Sensors')
plt.legend()
plt.grid(True)
plt.show()

# Research Extension: Add a queuing model (M/M/1) for sensor data processing.
# Test with different bandwidths (e.g., 1 Gbps for 6G).
# Explore AI inference latency at edge using frameworks like TensorFlow Lite.
```