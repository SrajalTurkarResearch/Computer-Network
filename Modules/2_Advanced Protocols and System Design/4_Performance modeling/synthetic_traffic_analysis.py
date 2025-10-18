import numpy as np
import matplotlib.pyplot as plt


def analyze_synthetic_traffic(lambda_rate=10, size=1000):
    """
    Generate and visualize synthetic packet arrivals using Poisson distribution.
    Simulates network traffic for analysis.
    Parameters:
        lambda_rate: Average arrival rate (packets/interval)
        size: Number of intervals
    """
    np.random.seed(42)  # For reproducibility
    arrivals = np.random.poisson(lam=lambda_rate, size=size)

    plt.hist(arrivals, bins=20, color="green", alpha=0.7)
    plt.title("Synthetic Packet Arrivals (Poisson Distribution)")
    plt.xlabel("Packets per Interval")
    plt.ylabel("Frequency")
    plt.grid(True)
    plt.show()

    print(f"Mean Arrivals: {np.mean(arrivals):.2f} packets/interval")
    print(f"Variance: {np.var(arrivals):.2f}")


if __name__ == "__main__":
    analyze_synthetic_traffic()
