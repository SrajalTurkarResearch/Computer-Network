# dijkstra_routing.py
"""
Tutorial File 1: Simulating OSPF Routing with Dijkstra’s Algorithm
Purpose: Learn how OSPF (Open Shortest Path First) finds the fastest paths in a network using Dijkstra’s algorithm.
This script creates a simple network, computes shortest paths, and visualizes the topology.
For aspiring scientists: Experiment with different link costs to study performance.
"""

# Import libraries (install with: pip install networkx matplotlib)
import networkx as nx
import matplotlib.pyplot as plt
from heapq import heappush, heappop


# Define Dijkstra’s algorithm to find shortest paths (like OSPF uses)
def dijkstra(graph, start):
    """
    Find shortest paths from start node to all others.
    graph: Dictionary with nodes and edge weights (e.g., {'R1': {'R2': 1, 'R3': 4}})
    start: Starting node (e.g., 'R1')
    Returns: Dictionary of shortest distances
    """
    queue = []
    heappush(queue, (0, start))  # (distance, node)
    distances = {node: float("inf") for node in graph}  # Start with infinite distances
    distances[start] = 0  # Distance to self is 0
    while queue:
        current_distance, current_node = heappop(queue)
        for neighbor, weight in graph[current_node].items():
            distance = current_distance + weight
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heappush(queue, (distance, neighbor))
    return distances


# Create a sample network (like routers in a city)
graph = {
    "R1": {"R2": 1, "R3": 4},  # R1 to R2: cost 1, R1 to R3: cost 4
    "R2": {"R1": 1, "R3": 2},  # R2 to R1: cost 1, R2 to R3: cost 2
    "R3": {"R1": 4, "R2": 2},  # R3 to R1: cost 4, R3 to R2: cost 2
}

# Run Dijkstra’s algorithm from R1
distances = dijkstra(graph, "R1")
print("Shortest distances from R1:", distances)
# Example output: {'R1': 0, 'R2': 1, 'R3': 3} (R1 to R3 via R2 is shorter)

# Visualize the network
G = nx.Graph()
G.add_edge("R1", "R2", weight=1)
G.add_edge("R2", "R3", weight=2)
G.add_edge("R1", "R3", weight=4)

pos = nx.spring_layout(G)  # Position nodes for plotting
nx.draw(G, pos, with_labels=True, node_color="lightblue", node_size=500)
labels = nx.get_edge_attributes(G, "weight")
nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)
plt.title("Network Topology (OSPF-like, Costs as Weights)")
plt.show()

# For Scientists: Research Idea
"""
Try changing edge weights to simulate bandwidth (e.g., weight = 10^8/bandwidth).
Explore how OSPF adapts to link failures (set a weight to infinity).
Check recent studies (e.g., 2024 MDPI on TOM-optimized OSPF for QoS).
"""
