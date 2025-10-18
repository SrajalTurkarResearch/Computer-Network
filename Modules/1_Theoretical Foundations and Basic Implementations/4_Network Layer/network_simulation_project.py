# network_simulation_project.py
# Major project: Simulate network with failures and analyze routing resilience
# Requires networkx: pip install networkx

import networkx as nx
from routing_algorithms import dijkstra
import random


def simulate_network_failure(nodes=10, edge_prob=0.3, source="0", dest="9"):
    """
    Simulate a random network, induce a failure, and recompute paths.

    Args:
        nodes (int): Number of nodes
        edge_prob (float): Probability of edge creation
        source (str): Source node
        dest (str): Destination node

    Returns:
        tuple: (original path, path after failure)
    """
    # Create random graph
    G = nx.erdos_renyi_graph(nodes, edge_prob)
    graph_dict = {str(i): {} for i in range(nodes)}
    for u, v in G.edges():
        weight = random.randint(1, 10)
        graph_dict[str(u)][str(v)] = weight
        graph_dict[str(v)][str(u)] = weight

    # Compute original shortest path
    original_dist = dijkstra(graph_dict, source)
    original_path = (
        nx.shortest_path(G, source, dest, weight="weight")
        if dest in original_dist
        else []
    )

    # Simulate failure: Remove a random edge
    edges = list(G.edges())
    if edges:
        edge_to_remove = random.choice(edges)
        G.remove_edge(*edge_to_remove)
        graph_dict = {str(i): {} for i in range(nodes)}
        for u, v in G.edges():
            weight = random.randint(1, 10)
            graph_dict[str(u)][str(v)] = weight
            graph_dict[str(v)][str(u)] = weight

    # Recompute path after failure
    new_dist = dijkstra(graph_dict, source)
    new_path = (
        nx.shortest_path(G, source, dest, weight="weight") if dest in new_dist else []
    )

    return original_path, new_path


# Example usage
if __name__ == "__main__":
    orig_path, new_path = simulate_network_failure()
    print(f"Original path: {orig_path}")
    print(f"Path after failure: {new_path}")
