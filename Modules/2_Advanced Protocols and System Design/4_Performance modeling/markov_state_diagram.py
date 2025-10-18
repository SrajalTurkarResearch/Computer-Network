import networkx as nx
import matplotlib.pyplot as plt


def plot_state_diagram():
    """
    Visualize a two-state Markov chain (Idle/Busy) as a directed graph.
    Nodes represent states, edges show transition probabilities.
    Requires NetworkX and Matplotlib.
    """
    # Create directed graph
    G = nx.DiGraph()
    G.add_edge("Idle", "Idle", weight=0.8)
    G.add_edge("Idle", "Busy", weight=0.2)
    G.add_edge("Busy", "Idle", weight=0.3)
    G.add_edge("Busy", "Busy", weight=0.7)

    # Layout and draw
    pos = nx.spring_layout(G)
    nx.draw(
        G, pos, with_labels=True, node_color="lightblue", node_size=2000, font_size=12
    )
    labels = nx.get_edge_attributes(G, "weight")
    nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)
    plt.title("Markov Chain State Diagram (Idle/Busy)")
    plt.show()


if __name__ == "__main__":
    plot_state_diagram()
