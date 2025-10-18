# red_simulation.py
# A standalone script to simulate Random Early Detection (RED) for QoS congestion avoidance.
# Models probabilistic packet drops, inspired by Einstein's insights into system stability.
# Requires: numpy, random

import numpy as np
import random


def red_simulation(arrivals, min_th=5, max_th=15, max_p=0.1, w=0.002):
    """
    Simulate RED congestion avoidance.

    Parameters:
    - arrivals (array): Arrival times of packets (seconds).
    - min_th (int): Minimum queue threshold for drops.
    - max_th (int): Maximum queue threshold for drops.
    - max_p (float): Maximum drop probability.
    - w (float): Weight for exponential moving average.

    Returns:
    - drop_rate (float): Fraction of packets dropped.
    """
    q_avg = 0
    queue = []
    drops = []

    for arrival in arrivals:
        # Update queue and average queue size
        q_len = len(queue)
        q_avg = (1 - w) * q_avg + w * q_len

        # RED logic
        if q_avg < min_th:
            queue.append(arrival)  # No drops
        elif q_avg < max_th:
            # Probabilistic drop
            p_drop = max_p * (q_avg - min_th) / (max_th - min_th)
            if random.random() > p_drop:
                queue.append(arrival)  # Keep packet
            else:
                drops.append(arrival)  # Drop packet
        else:
            drops.append(arrival)  # Drop all if queue too large

    # Simulate packet departure (simplified: immediate service for kept packets)
    drop_rate = len(drops) / len(arrivals) if arrivals else 0
    return drop_rate


if __name__ == "__main__":
    # Generate 1000 packet arrivals with exponential inter-arrival times (λ=0.8)
    np.random.seed(42)  # For reproducibility
    arrivals = np.cumsum(np.random.exponential(1 / 0.8, 1000))

    # RED parameters
    min_th = 5
    max_th = 15
    max_p = 0.1
    w = 0.002

    # Run simulation
    drop_rate = red_simulation(arrivals, min_th, max_th, max_p, w)

    # Print results
    print(f"RED Simulation Results:")
    print(f"Drop Rate: {drop_rate:.4f} (fraction of packets dropped)")
    print(f"Parameters: min_th={min_th}, max_th={max_th}, max_p={max_p}, w={w}")
