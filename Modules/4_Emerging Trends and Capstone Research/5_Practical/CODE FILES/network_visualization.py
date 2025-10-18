# network_visualization.py
# Purpose: Visualize a simple SDN topology (2 hosts, 1 switch) using NetworkX
# and simulate network traffic with Matplotlib. This helps understand network
# structure and performance, critical for SDN/NFV prototyping.
# Usage: Run with `python3 network_visualization.py` in a Ubuntu environment
# with NetworkX, Matplotlib, and NumPy installed (`pip3 install networkx matplotlib numpy`).
# Learning Objective: Learn to visualize network topologies and analyze traffic
# patterns, essential for designing and testing SDN systems.

import networkx as nx
import matplotlib.pyplot as plt
import numpy as np

# Create a simple network graph (2 hosts connected to 1 switch)
G = nx.Graph()
G.add_nodes_from(["h1", "h2", "s1"])  # Hosts and switch as nodes
G.add_edges_from([("h1", "s1"), ("h2", "s1")])  # Links between hosts and switch

# Visualize the topology
plt.figure(figsize=(6, 4))
pos = nx.spring_layout(G)  # Position nodes for clean layout
nx.draw(G, pos, with_labels=True, node_color="lightblue", node_size=500, font_size=10)
plt.title("Simple SDN Topology")
plt.show()

# Simulate network traffic (packets per second over time)
time = np.arange(0, 10, 0.1)  # Time from 0 to 10 seconds
traffic = np.sin(time) * 100 + 200  # Simulated traffic pattern (sinusoidal)
plt.figure(figsize=(8, 5))
plt.plot(time, traffic, label="Traffic Load")
plt.xlabel("Time (s)")
plt.ylabel("Packets/s")
plt.title("Simulated Network Traffic")
plt.legend()
plt.grid()
plt.show()

# Notes for Aspiring Scientist:
# - The topology visualization shows how hosts connect via a switch, reflecting
#   the Mininet setup in simple_sdn.py.
# - The traffic plot simulates load (e.g., packets/s). In real SDN, controllers
#   monitor such patterns to optimize flows.
# - Research Idea: Modify traffic pattern (e.g., add noise with np.random.normal)
#   and hypothesize how SDN controllers handle bursts. Test with Mininet’s iperf.
