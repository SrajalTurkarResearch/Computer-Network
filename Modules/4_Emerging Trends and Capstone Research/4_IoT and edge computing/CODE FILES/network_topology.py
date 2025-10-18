```python
# network_topology.py
# Purpose: Model and visualize a mesh network topology for IoT devices.
# Context: IoT networks use topologies like mesh (every device connects to all others)
# to ensure robust communication. This script creates a 5-device mesh network and counts links.
# Requirements: networkx, matplotlib

import networkx as nx
import matplotlib.pyplot as plt

# Create a mesh network of 5 devices
G = nx.complete_graph(5)  # Every node connects to all others
print(f"Mesh network links: {G.number_of_edges()}")

# Visualize the network
plt.figure(figsize=(6, 6))
nx.draw(G, with_labels=True, node_color='lightblue', node_size=500, font_size=12)
plt.title('Mesh Network Topology (5 Devices)')
plt.show()
```