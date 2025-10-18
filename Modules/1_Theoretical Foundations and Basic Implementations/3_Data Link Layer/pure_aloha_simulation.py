# Pure ALOHA Simulation for Data Link Layer
# Created by Grok 4, xAI, for aspiring scientists and researchers
# Date: September 09, 2025
#
# Purpose: Simulate Pure ALOHA, a MAC protocol where devices send frames randomly,
# leading to collisions if frames overlap within 2x frame time. Derives throughput
# S = G * e^(-2G), max ~0.184 at G=0.5 (from Poisson arrivals). Visualize to confirm.
#
# Why: Understand shared medium access, critical for IoT, satellite networks.
# Research: Modify G, frame_time, or add slotted ALOHA for comparison.
#
# Dependencies: numpy, matplotlib (pip install numpy matplotlib)

import random
import numpy as np
import matplotlib.pyplot as plt


def simulate_pure_aloha(num_frames=1000, G=0.5, frame_time=1.0):
    """
    Simulate Pure ALOHA with Poisson arrivals.
    Parameters:
        num_frames (int): Number of frames to simulate.
        G (float): Offered load (average frames per frame time).
        frame_time (float): Duration of one frame (arbitrary units).
    Returns:
        S (float): Throughput (successful frames per unit time).
    """
    # Derive Poisson rate: lambda = G / frame_time
    lambda_rate = G / frame_time
    send_times = []
    t = 0
    # Generate random send times (exponential inter-arrivals)
    for _ in range(num_frames):
        t += random.expovariate(lambda_rate)
        send_times.append(t)

    # Check collisions: A frame at t collides if another starts in [t, t+2*frame_time]
    collisions = 0
    for i in range(num_frames):
        start = send_times[i]
        end = start + frame_time
        collided = False
        for j in range(i + 1, num_frames):
            # Optimization: Stop checking if beyond vulnerability period
            if send_times[j] >= end + frame_time:
                break
            # Collision if another frame starts within 2*frame_time
            if send_times[j] < end + frame_time:
                collided = True
                break
        if collided:
            collisions += 1

    # Calculate throughput: successful frames / total time
    successful = num_frames - collisions
    total_time = send_times[-1] + frame_time
    S = successful * frame_time / total_time
    return S


def plot_aloha_throughput():
    """
    Plot theoretical vs. simulated Pure ALOHA throughput.
    Theory: S = G * e^(-2G), max at G=0.5 (S≈0.184).
    """
    # Simulate for various G values
    G_values = np.linspace(0.1, 2.0, 20)
    S_simulated = [simulate_pure_aloha(1000, g) for g in G_values]
    S_theoretical = G_values * np.exp(-2 * G_values)

    plt.figure(figsize=(8, 6))
    plt.plot(G_values, S_theoretical, label="Theoretical S = G * e^(-2G)", color="blue")
    plt.plot(G_values, S_simulated, "ro", label="Simulated", alpha=0.5)
    plt.xlabel("Offered Load (G)")
    plt.ylabel("Throughput (S)")
    plt.title("Pure ALOHA Throughput: Theory vs. Simulation")
    plt.legend()
    plt.grid(True)
    plt.show()


if __name__ == "__main__":
    # Run a single simulation at G=0.5
    S = simulate_pure_aloha(1000, 0.5)
    print(f"Simulated Throughput at G=0.5: {S:.3f} (theoretical max ~0.184)")

    # Plot throughput curve
    plot_aloha_throughput()

    # Research Extension: Try G=1.0, add Slotted ALOHA (S = G * e^(-G)),
    # or modify frame_time for IoT scenarios (e.g., low-power sensors).
