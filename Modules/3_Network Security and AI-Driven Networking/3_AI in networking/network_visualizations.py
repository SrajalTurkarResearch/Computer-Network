"""
network_visualizations.py

Generates visualizations for network topology (star) and traffic patterns.
Designed for researchers to understand network structures and dynamics visually.

Dependencies: numpy, matplotlib
Run: python network_visualizations.py
"""

import numpy as np
import matplotlib.pyplot as plt


def plot_star_topology():
    """Plot a star network topology with a central hub and connected nodes."""
    fig, ax = plt.subplots(figsize=(8, 6))
    # Central hub
    ax.add_patch(plt.Circle((0.5, 0.5), 0.1, color="red", label="Hub"))
    # Peripheral nodes
    for i in range(4):
        angle = i * 90
        x = 0.5 + 0.3 * np.cos(np.radians(angle))
        y = 0.5 + 0.3 * np.sin(np.radians(angle))
        ax.add_patch(
            plt.Circle((x, y), 0.05, color="blue", label="Node" if i == 0 else "")
        )
        ax.plot([0.5, x], [0.5, y], "k--")  # Connections
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.set_title("Star Network Topology")
    ax.axis("off")
    ax.legend()
    plt.show()


def plot_traffic_pattern():
    """Plot a synthetic daily network traffic pattern."""
    time = np.arange(0, 24, 1)
    traffic = 50 + 30 * np.sin(2 * np.pi * time / 24) + np.random.normal(0, 10, 24)
    plt.figure(figsize=(10, 4))
    plt.plot(time, traffic, label="Traffic Volume")
    plt.title("Daily Network Traffic Pattern")
    plt.xlabel("Time (Hours)")
    plt.ylabel("Traffic Volume")
    plt.grid(True)
    plt.legend()
    plt.show()


def main():
    print("Generating Network Topology Visualization...")
    plot_star_topology()
    print("Generating Traffic Pattern Visualization...")
    plot_traffic_pattern()


if __name__ == "__main__":
    main()
