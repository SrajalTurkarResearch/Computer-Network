# bellman_ford.py
"""
Tutorial File 3: Implementing Bellman-Ford for Distance Vector Routing
Purpose: Learn how distance vector protocols (like RIP) find paths using Bellman-Ford.
This script implements the algorithm and solves an exercise.
For aspiring scientists: Test with negative weights or larger networks.
"""


# Implement Bellman-Ford algorithm
def bellman_ford(graph, start):
    """
    Find shortest paths using Bellman-Ford (used in RIP-like protocols).
    graph: Dictionary with nodes and edge weights
    start: Starting node
    Returns: Dictionary of shortest distances
    """
    distances = {node: float("inf") for node in graph}
    distances[start] = 0
    for _ in range(len(graph) - 1):  # Run V-1 times
        for u in graph:
            for v, weight in graph[u].items():
                if distances[u] + weight < distances[v]:
                    distances[v] = distances[u] + weight
    return distances


# Sample network
graph = {"R1": {"R2": 1, "R3": 4}, "R2": {"R1": 1, "R3": 2}, "R3": {"R1": 4, "R2": 2}}

# Run Bellman-Ford from R1
distances = bellman_ford(graph, "R1")
print("Shortest distances from R1 (Bellman-Ford):", distances)
# Example output: {'R1': 0, 'R2': 1, 'R3': 3}

# Exercise Solution: Add a new node and test
"""
Exercise: Add a node 'R4' with edges R3->R4 (weight 1), R4->R2 (weight 3).
Test if Bellman-Ford finds correct paths.
"""
new_graph = {
    "R1": {"R2": 1, "R3": 4},
    "R2": {"R1": 1, "R3": 2, "R4": 3},
    "R3": {"R1": 4, "R2": 2, "R4": 1},
    "R4": {"R2": 3, "R3": 1},
}
print("With new node R4:", bellman_ford(new_graph, "R1"))

# For Scientists: Research Idea
"""
Test Bellman-Ford with negative weights (rare in networking but useful for theory).
Explore its use in EIGRP (Cisco’s advanced distance vector protocol).
Check 2024 fuzzy cuckoo search papers for optimization insights.
"""
