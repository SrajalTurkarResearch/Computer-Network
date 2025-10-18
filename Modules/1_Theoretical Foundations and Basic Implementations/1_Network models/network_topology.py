# network_topology.py
# Simulates a hybrid network topology (Hybrid Architecture)
# Purpose: Visualize and analyze network structure
# Relevance: Models real-world networks (e.g., cloud, IoT) using NetworkX
# Install: pip install networkx matplotlib

import networkx as nx
import matplotlib.pyplot as plt


def create_topology():
    """Create and visualize a hybrid network topology."""
    # Create graph
    G = nx.Graph()
    # Nodes: Router (L3), Switch (L2), PCs (L7), Cloud (Hybrid)
    G.add_nodes_from(["Router", "Switch", "PC1", "PC2", "Cloud"])
    # Edges: Simulate network connections
    G.add_edges_from(
        [
            ("Router", "Switch"),
            ("Switch", "PC1"),
            ("Switch", "PC2"),
            ("Router", "Cloud"),
        ]
    )

    # Visualize
    plt.figure(figsize=(8, 6))
    nx.draw(
        G,
        with_labels=True,
        node_color="skyblue",
        node_size=2000,
        font_size=12,
        font_weight="bold",
    )
    plt.title("Hybrid Network Topology (Router-Switch-Cloud)")
    plt.show()

    # Analyze shortest path (L3 routing)
    path = nx.shortest_path(G, "PC1", "Cloud")
    print(f"Shortest path from PC1 to Cloud: {path}")


if __name__ == "__main__":
    create_topology()

# Research Insight: Topology analysis optimizes routing (e.g., in SDN for 5G networks).
# Example: Models AWS cloud interconnectivity for hybrid architectures.
# Next Step: Add weights (latency) to edges for performance analysis in experiments.
