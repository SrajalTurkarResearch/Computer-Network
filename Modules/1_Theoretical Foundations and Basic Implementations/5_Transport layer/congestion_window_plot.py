# congestion_window_plot.py
# Plots TCP congestion window growth (slow start, avoidance, loss)
# Requires matplotlib: pip install matplotlib
# Scientist note: Adjust cwnd values to model BBR or CUBIC

import matplotlib.pyplot as plt
import sys

try:
    # Simulated RTTs and cwnd (in MSS units)
    rtt = list(range(1, 11))  # 10 RTTs
    cwnd = [1, 2, 4, 8, 16, 17, 18, 19, 10, 11]  # Slow start, then linear, loss at 8
    plt.plot(rtt, cwnd, marker="o", color="blue")
    plt.xlabel("RTT (Round-Trip Time)")
    plt.ylabel("Congestion Window (MSS)")
    plt.title("TCP Congestion Window Evolution")
    plt.grid(True)
    plt.show()
except ImportError:
    print("Install matplotlib: pip install matplotlib")
    sys.exit(1)
except Exception as e:
    print(f"Error: {e}")
    sys.exit(1)
