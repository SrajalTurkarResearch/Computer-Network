"""
convergence_times.py
Simulates and plots convergence times for OSPF and BGP.
Shows OSPF's O(n log n) vs. BGP's O(n^3) complexity.
Requires: numpy, matplotlib
Run: python convergence_times.py
"""

import numpy as np
import matplotlib.pyplot as plt

# Simulate convergence times for different network sizes
network_sizes = np.arange(10, 100, 10)
ospf_times = network_sizes * np.log(network_sizes) / 1000  # OSPF: O(n log n)
bgp_times = network_sizes**3 / 1e6  # BGP: Worst-case O(n^3)

# Plot the results
plt.plot(network_sizes, ospf_times, label="OSPF", color="blue")
plt.plot(network_sizes, bgp_times, label="BGP", color="red")
plt.xlabel("Network Size (Nodes)")
plt.ylabel("Convergence Time (ms)")
plt.title("Simulated Convergence Times: OSPF vs. BGP")
plt.legend()
plt.grid(True)
plt.show()

"""
Explanation:
- OSPF converges faster due to efficient link-state flooding and Dijkstra.
- BGP is slower due to policy propagation across ASes.
- Plot shows how OSPF scales better than BGP for larger networks.
- Useful for understanding real-world delays (e.g., 2020 Cloudflare outage).
"""
