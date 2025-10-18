# network_visualization.py
# Visualize centralized and decentralized networks for educational purposes.

import networkx as nx
import matplotlib.pyplot as plt

# Centralized Network (Star Graph)
G_central = nx.star_graph(5)
nx.draw(G_central, with_labels=True)
plt.title("Centralized Network")
plt.show()

# Decentralized Network (Random Geometric Graph)
G_decentral = nx.random_geometric_graph(10, 0.3)
nx.draw(G_decentral, with_labels=True)
plt.title("Decentralized Network")
plt.show()

# To run: python network_visualization.py
# Requires: networkx, matplotlib (available in the code execution environment)
