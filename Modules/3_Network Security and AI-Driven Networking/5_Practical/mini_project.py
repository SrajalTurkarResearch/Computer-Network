# mini_project.py
# Mini project: Models a complete (mesh) graph and analyzes edges.
# Explores network redundancy.

import networkx as nx
import matplotlib.pyplot as plt

# Create full mesh with 5 nodes
G = nx.complete_graph(5)

# Draw and display
nx.draw(G, with_labels=True, node_color="lightgreen", edge_color="blue")
plt.title("Mesh Topology Mini Project")
plt.show()

# Analysis
num_edges = G.number_of_edges()
print(f"Number of edges in mesh: {num_edges}")
print("This demonstrates high connectivity; ideal for fault-tolerant networks.")
