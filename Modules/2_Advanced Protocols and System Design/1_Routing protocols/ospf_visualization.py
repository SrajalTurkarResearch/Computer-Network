"""
ospf_visualization.py
Visualizes an OSPF network topology using NetworkX and Matplotlib.
Shows routers and links with costs.
Requires: networkx, matplotlib
Run: python ospf_visualization.py
"""

import networkx as nx
import matplotlib.pyplot as plt

# Create OSPF network graph
G = nx.Graph()
G.add_edge("R1", "R2", weight=10)  # R1-R2: cost=10
G.add_edge("R1", "R3", weight=15)  # R1-R3: cost=15
G.add_edge("R2", "R3", weight=5)  # R2-R3: cost=5

# Draw the graph
pos = nx.spring_layout(G)
nx.draw(G, pos, with_labels=True, node_color="lightblue", node_size=500, font_size=10)
labels = nx.get_edge_attributes(G, "weight")
nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)
plt.title("OSPF Network Topology")
plt.show()

"""
Explanation:
- NetworkX creates a graph with routers (R1, R2, R3) and weighted links.
- Spring layout positions nodes for clarity.
- Edge labels show costs, reflecting OSPF's link-state metrics.
- Helps visualize how OSPF builds its topology map (LSDB).
"""
