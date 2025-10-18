# network_topology.py
# Visualizes a star network topology.
# Useful for studying connectivity in computer networks.

import networkx as nx
import matplotlib.pyplot as plt

# Create star graph with 5 peripheral nodes
G = nx.star_graph(5)

# Draw and display
nx.draw(G, with_labels=True, node_color="lightblue", edge_color="gray")
plt.title("Star Topology Visualization")
plt.show()

print("Star topology plotted. Central node connected to 5 others.")
