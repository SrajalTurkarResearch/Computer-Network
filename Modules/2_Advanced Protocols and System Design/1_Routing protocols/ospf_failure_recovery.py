"""
ospf_failure_recovery.py
Simulates OSPF failure recovery by removing a link and recomputing paths.
Demonstrates OSPF's fast convergence.
Requires: networkx
Run: python ospf_failure_recovery.py
"""

import networkx as nx

# Create initial OSPF network
G = nx.Graph()
G.add_edge("R1", "R2", weight=10)
G.add_edge("R1", "R3", weight=15)
G.add_edge("R2", "R3", weight=5)

# Initial shortest path
try:
    path = nx.dijkstra_path(G, "R1", "R3", weight="weight")
    cost = nx.dijkstra_path_length(G, "R1", "R3", weight="weight")
    print(f"Initial Path: {path}, Cost: {cost}")
except nx.NetworkXNoPath:
    print("No initial path exists")

# Simulate link failure (R1-R3 breaks)
G.remove_edge("R1", "R3")
try:
    new_path = nx.dijkstra_path(G, "R1", "R3", weight="weight")
    new_cost = nx.dijkstra_path_length(G, "R1", "R3", weight="weight")
    print(f"New Path after Failure: {new_path}, Cost: {new_cost}")
except nx.NetworkXNoPath:
    print("No path exists after failure")

"""
Explanation:
- Simulates a link failure (R1-R3) in an OSPF network.
- Recomputes paths using Dijkstra, showing OSPF's ability to reroute (e.g., R1->R2->R3).
- Reflects OSPF's fast convergence (~0.5s in real networks).
"""
