import numpy as np
import matplotlib.pyplot as plt


def plot_latency_vs_utilization(mu_rate=15):
    """
    Plot queuing delay (W_q) vs. utilization (ρ) for M/M/1 queue.
    Parameters:
        mu_rate: Service rate (packets/sec)
    """
    rho = np.linspace(0.01, 0.99, 100)  # Utilization from 0.01 to 0.99
    W_q = 1 / (mu_rate * (1 - rho)) - 1 / mu_rate  # System time (ms)

    plt.plot(rho, W_q * 1000, color="blue")
    plt.xlabel("Utilization (ρ)")
    plt.ylabel("Average Delay (ms)")
    plt.title("Latency vs. Utilization in M/M/1 Queue")
    plt.grid(True)
    plt.show()


if __name__ == "__main__":
    plot_latency_vs_utilization()
