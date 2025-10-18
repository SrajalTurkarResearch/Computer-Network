# traffic_analysis.py
# Analyzes 5G traffic dataset (e.g., from Kaggle)
# Purpose: Visualize traffic patterns for real-world 5G applications
# Note: Requires '5g_traffic.csv' from Kaggle (e.g., https://www.kaggle.com/datasets/kimdaegyeom/5g-traffic-datasets)
# Usage: Download dataset, update path, run to plot traffic volume

import pandas as pd
import matplotlib.pyplot as plt


def plot_traffic_data(csv_path):
    """
    Plot 5G traffic volume over time
    Parameters:
        csv_path (str): Path to CSV file
    """
    try:
        # Load dataset
        df = pd.read_csv(csv_path)
        # Plot time vs. traffic volume
        plt.figure(figsize=(10, 6))
        df.plot(x="time", y="traffic_volume")
        plt.xlabel("Time")
        plt.ylabel("Traffic Volume (Mbps)")
        plt.title("5G Network Traffic Analysis")
        plt.grid(True)
        plt.show()
    except FileNotFoundError:
        print("Error: Please download '5g_traffic.csv' and update the path.")


# Example usage
csv_path = "5g_traffic.csv"  # Replace with actual path
plot_traffic_data(csv_path)
# Expected: Line plot of traffic volume vs. time (if dataset available)
