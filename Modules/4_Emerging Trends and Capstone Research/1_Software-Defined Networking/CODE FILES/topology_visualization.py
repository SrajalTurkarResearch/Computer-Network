# topology_visualization.py
# Visualizes an SDN network topology using NetworkX and Matplotlib.
# Purpose: Help beginners understand SDN structure visually.
# Requirements: Install NetworkX and Matplotlib (`pip install networkx matplotlib`).
# Usage: Run directly (`python topology_visualization.py`) to display a graph.

import networkx as nx
import matplotlib.pyplot as plt

# Create a simple SDN topology
G = nx.Graph()
# Nodes: Controller, switches (S1, S2, S3), hosts (H1, H2)
G.add_nodes_from(["Controller", "S1", "S2", "S3", "H1", "H2"])
# Edges: Controller connects to switches, switches connect to each other and hosts
G.add_edges_from(
    [
        ("Controller", "S1"),
        ("Controller", "S2"),
        ("Controller", "S3"),
        ("S1", "S2"),
        ("S2", "S3"),
        ("S1", "H1"),
        ("S3", "H2"),
    ]
)

# Plot the topology
plt.figure(figsize=(8, 6))
pos = nx.spring_layout(G)  # Layout for node positioning
nx.draw(G, pos, with_labels=True, node_color="lightblue", node_size=500, font_size=12)
plt.title("SDN Network Topology")
plt.show()

# Notes for scientists:
# - Sketch this topology in your notebook to understand SDN’s centralized control.
# - Research idea: Visualize dynamic topologies (e.g., changing links based on traffic).
