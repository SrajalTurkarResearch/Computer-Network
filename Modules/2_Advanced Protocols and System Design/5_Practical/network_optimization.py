# network_optimization.py
"""
Tutorial File 4: Network Performance Optimization with Queuing Theory
Purpose: Understand network performance (latency, throughput) using M/M/1 queuing model.
This script calculates queue metrics and visualizes traffic.
For aspiring scientists: Experiment with arrival/service rates or use real datasets.
"""

# Import libraries (install with: pip install matplotlib scipy)
import matplotlib.pyplot as plt
import numpy as np


# M/M/1 Queuing Model
def mm1_queue_metrics(arrival_rate, service_rate):
    """
    Calculate M/M/1 queue metrics (like a router’s packet queue).
    arrival_rate: Packets per second (lambda)
    service_rate: Packets processed per second (mu)
    Returns: Waiting time, queue length
    """
    if arrival_rate >= service_rate:
        return None, None  # Queue unstable
    waiting_time = 1 / (service_rate - arrival_rate)  # W = 1/(mu - lambda)
    queue_length = arrival_rate * waiting_time  # L = lambda * W (Little’s Law)
    return waiting_time, queue_length


# Simulate different traffic loads
arrival_rates = np.linspace(10, 90, 9)  # Packets per second
service_rate = 100  # Packets per second
waiting_times = []
queue_lengths = []

for lam in arrival_rates:
    w, l = mm1_queue_metrics(lam, service_rate)
    waiting_times.append(w if w else float("inf"))
    queue_lengths.append(l if l else float("inf"))

# Plot results
plt.figure(figsize=(10, 5))
plt.subplot(1, 2, 1)
plt.plot(arrival_rates, waiting_times, "b-o")
plt.xlabel("Arrival Rate (packets/s)")
plt.ylabel("Waiting Time (s)")
plt.title("M/M/1 Queue: Waiting Time")
plt.grid(True)

plt.subplot(1, 2, 2)
plt.plot(arrival_rates, queue_lengths, "r-o")
plt.xlabel("Arrival Rate (packets/s)")
plt.ylabel("Queue Length (packets)")
plt.title("M/M/1 Queue: Queue Length")
plt.grid(True)
plt.tight_layout()
plt.show()

# Example output
lam, mu = 50, 100
w, l = mm1_queue_metrics(lam, mu)
print(f"For arrival rate {lam}, service rate {mu}:")
print(f"Waiting time: {w:.3f} seconds, Queue length: {l:.1f} packets")

# For Scientists: Research Idea
"""
Use real traffic data (e.g., UOS_IOTSH_2024 dataset) to test queuing models.
Explore advanced models like M/G/1 or Markov chains for IoT networks.
Check 2025 RouteNet-Fermi for AI-based performance prediction.
"""
