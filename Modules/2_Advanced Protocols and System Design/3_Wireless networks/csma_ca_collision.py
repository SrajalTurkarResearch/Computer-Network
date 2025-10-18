# csma_ca_collision.py
# Simulates CSMA/CA collision probability for multiple devices
# Purpose: Understand how contention affects wireless network performance
# Math: p ≈ 1/(CW+1) per device, effective p = 1 - (1-p)^n for n devices
# Usage: Run to simulate and print collision probability

import random


def simulate_csma_ca(n_devices, CW=15, trials=1000):
    """
    Simulate CSMA/CA collisions
    Parameters:
        n_devices (int): Number of devices
        CW (int): Contention window size
        trials (int): Number of simulation runs
    Returns:
        float: Collision probability
    """
    collisions = 0
    for _ in range(trials):
        # Each device picks random backoff slot (0 to CW)
        backoffs = [random.randint(0, CW) for _ in range(n_devices)]
        # Collision if any backoff slots are identical
        if len(set(backoffs)) < n_devices:
            collisions += 1
    return collisions / trials


# Parameters
n_devices = 10  # Number of devices
CW = 15  # Initial contention window

# Run simulation
p_sim = simulate_csma_ca(n_devices, CW)
print(f"Collision Probability for {n_devices} devices (CW={CW}): {p_sim:.2f}")
# Expected: ~0.47 (analytical: 1 - (1-1/16)^10 ≈ 0.47)
