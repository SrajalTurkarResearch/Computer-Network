"""
dijkstra_ospf.py
Simulates Dijkstra's algorithm for OSPF routing in a network.
Used to find shortest paths from a source router to all destinations.
Requires: networkx, matplotlib for graph and visualization.
Run: python dijkstra_ospf.py
"""

import networkx as nx
import matplotlib.pyplot as plt

# Create a sample network graph for OSPF simulation
# Routers: R1, R2, R3; Links with costs (e.g., based on 100Mbps/LinkSpeed)
G = nx.Graph()
G.add_edge("R1", "R2", weight=10)  # R1-R2: 1Gbps -> cost=10
G.add_edge("R1", "R3", weight=15)  # R1-R3: 100Mbps -> cost=15
G.add_edge("R2", "R3", weight=5)  # R2-R3: 10Gbps -> cost=5

# Compute shortest path from R1 to R3 using Dijkstra's algorithm
try:
    path = nx.dijkstra_path(G, "R1", "R3", weight="weight")
    cost = nx.dijkstra_path_length(G, "R1", "R3", weight="weight")
    print(f"Shortest Path: {path}, Cost: {cost}")
except nx.NetworkXNoPath:
    print("No path exists between R1 and R3")

# Visualize the network
pos = nx.spring_layout(G)
nx.draw(G, pos, with_labels=True, node_color="lightblue", node_size=500, font_size=10)
labels = nx.get_edge_attributes(G, "weight")
nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)
plt.title("OSPF Network Topology")
plt.show()

"""
Explanation:
- NetworkX creates a graph representing routers (nodes) and links (edges) with costs.
- Dijkstra's algorithm finds the shortest path (e.g., R1->R2->R3, cost=15).
- Visualization shows the topology with weighted edges.
- For OSPF, this simulates how routers compute paths based on the Link-State Database (LSDB).
"""
