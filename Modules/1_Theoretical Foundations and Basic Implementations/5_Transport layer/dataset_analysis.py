# dataset_analysis.py
# Analyzes network dataset for TCP/UDP usage
# Requires pandas, matplotlib: pip install pandas matplotlib
# Download CIC-DDoS2019 from https://www.unb.ca/cic/datasets/ddos-2019.html
# Scientist note: Extend to analyze SEQ numbers or retransmits

import pandas as pd
import matplotlib.pyplot as plt
import sys

try:
    # Replace 'data.csv' with your dataset path
    df = pd.read_csv("data.csv")  # Assumes CSV from CIC-DDoS2019
    # Plot protocol distribution (TCP=6, UDP=17 in IP headers)
    df["protocol"].value_counts().plot(kind="bar", color=["blue", "green"])
    plt.xlabel("Protocol (6=TCP, 17=UDP)")
    plt.ylabel("Packet Count")
    plt.title("TCP vs UDP in Network Traffic")
    plt.show()
except FileNotFoundError:
    print("Download dataset from https://www.unb.ca/cic/datasets/ddos-2019.html")
    sys.exit(1)
except ImportError:
    print("Install pandas and matplotlib: pip install pandas matplotlib")
    sys.exit(1)
except Exception as e:
    print(f"Error: {e}")
    sys.exit(1)
