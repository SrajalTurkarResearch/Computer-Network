# osi_visualization.py
# Visualizes OSI Model layers
# Purpose: Understand theoretical layering structure
# Relevance: OSI provides a universal framework for network analysis
# Install: pip install matplotlib

import matplotlib.pyplot as plt


def visualize_osi_model():
    """Visualize the 7-layer OSI model."""
    layers = [
        "Application",
        "Presentation",
        "Session",
        "Transport",
        "Network",
        "Data Link",
        "Physical",
    ]
    fig, ax = plt.subplots(figsize=(4, 6))

    # Plot layers as stacked boxes
    for i, layer in enumerate(reversed(layers)):
        ax.text(
            0.5,
            i,
            layer,
            ha="center",
            va="center",
            fontsize=12,
            bbox=dict(facecolor="skyblue", edgecolor="black", boxstyle="round,pad=0.3"),
        )

    # Add arrows for data flow
    for i in range(len(layers) - 1):
        ax.arrow(0.5, i + 0.5, 0, 0.5, head_width=0.05, head_length=0.1, fc="black")
        ax.arrow(0.5, i + 0.5, 0, -0.5, head_width=0.05, head_length=0.1, fc="black")

    ax.set_xlim(0, 1)
    ax.set_ylim(-0.5, len(layers))
    ax.axis("off")
    plt.title("OSI Model: Data Flow (Encapsulation/Decapsulation)")
    plt.show()


if __name__ == "__main__":
    visualize_osi_model()

# Research Insight: Visualizing layers aids in designing experiments (e.g., simulating L4 congestion).
# Example: Used in teaching network fundamentals for scientific applications.
# Next Step: Add protocol labels (e.g., HTTP, TCP) to layers for detailed visualization.
