# crypto_visualizations.py
# A Python script for visualizing cryptographic processes
# Purpose: Create flowcharts for symmetric/asymmetric encryption and a plot for Diffie-Hellman
# For aspiring scientists: Helps understand the flow and math visually

import matplotlib.pyplot as plt
import networkx as nx
import numpy as np


def plot_symmetric_flow():
    """Visualize the flow of symmetric encryption."""
    G = nx.DiGraph()
    G.add_edges_from(
        [
            ("Plaintext", "Encrypt with Key"),
            ("Encrypt with Key", "Ciphertext"),
            ("Ciphertext", "Decrypt with Key"),
            ("Decrypt with Key", "Plaintext"),
        ]
    )
    pos = nx.spring_layout(G)
    plt.figure(figsize=(8, 6))
    nx.draw(
        G, pos, with_labels=True, node_color="lightblue", node_size=2000, font_size=10
    )
    plt.title("Symmetric Encryption Flow (e.g., AES)")
    plt.show()


def plot_asymmetric_flow():
    """Visualize the flow of asymmetric encryption."""
    G = nx.DiGraph()
    G.add_edges_from(
        [
            ("Plaintext", "Encrypt with Public Key"),
            ("Encrypt with Public Key", "Ciphertext"),
            ("Ciphertext", "Decrypt with Private Key"),
            ("Decrypt with Private Key", "Plaintext"),
        ]
    )
    pos = nx.spring_layout(G)
    plt.figure(figsize=(8, 6))
    nx.draw(
        G, pos, with_labels=True, node_color="lightgreen", node_size=2000, font_size=10
    )
    plt.title("Asymmetric Encryption Flow (e.g., RSA)")
    plt.show()


def plot_dh_modular():
    """Visualize modular exponentiation in Diffie-Hellman."""
    x = np.arange(1, 11)
    y = (5**x) % 23
    plt.figure(figsize=(8, 6))
    plt.plot(x, y, marker="o")
    plt.title("Diffie-Hellman Modular Exponentiation (g=5, p=23)")
    plt.xlabel("Exponent")
    plt.ylabel("Result mod 23")
    plt.grid(True)
    plt.show()


def main():
    print("=== Cryptography Visualizations ===")
    print("Generating flowcharts and plots for cryptographic processes...")

    # Plot symmetric encryption flow
    print("1. Symmetric Encryption Flow")
    plot_symmetric_flow()

    # Plot asymmetric encryption flow
    print("2. Asymmetric Encryption Flow")
    plot_asymmetric_flow()

    # Plot Diffie-Hellman modular exponentiation
    print("3. Diffie-Hellman Modular Exponentiation")
    plot_dh_modular()


if __name__ == "__main__":
    main()
