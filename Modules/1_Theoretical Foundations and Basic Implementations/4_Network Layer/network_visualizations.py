# network_visualizations.py
# Visualizations for IP address space and network graphs
# Requires networkx and matplotlib: pip install networkx matplotlib

import networkx as nx
import matplotlib.pyplot as plt


def plot_ip_space():
    """
    Visualize IPv4 vs IPv6 address space on a logarithmic scale.
    """
    labels = ["IPv4", "IPv6"]
    sizes = [2**32, 2**128]
    plt.bar(labels, sizes, log=True, color=["blue", "green"])
    plt.ylabel("Addresses (log scale)")
    plt.title("IPv4 vs IPv6 Address Space Comparison")
    plt.show()


def plot_network_graph():
    """
    Visualize a sample network graph with weighted edges.
    """
    G = nx.Graph()
    G.add_edge("A", "B", weight=1)
    G.add_edge("A", "C", weight=5)
    G.add_edge("B", "C", weight=1)
    pos = nx.spring_layout(G)
    nx.draw(G, pos, with_labels=True, node_color="lightblue", node_size=500)
    labels = nx.get_edge_attributes(G, "weight")
    nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)
    plt.title("Sample Network Graph for Routing")
    plt.show()


# Example usage
if __name__ == "__main__":
    plot_ip_space()
    plot_network_graph()
