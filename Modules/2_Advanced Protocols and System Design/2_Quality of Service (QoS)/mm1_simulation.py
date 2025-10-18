# mm1_simulation.py
# A standalone script to simulate an M/M/1 queue for studying QoS in computer networks.
# Simulates packet arrivals (Poisson, rate λ) and service times (exponential, rate μ).
# Outputs average queue length and a plot, inspired by Turing's logical precision.
# Requires: numpy, matplotlib, random

import random
import numpy as np
import matplotlib.pyplot as plt


def mm1_simulation(lambda_, mu, sim_time=100, max_queue=float("inf")):
    """
    Simulate an M/M/1 queue or M/M/1/K if max_queue is specified.

    Parameters:
    - lambda_ (float): Arrival rate (packets per second).
    - mu (float): Service rate (packets per second).
    - sim_time (float): Total simulation time (seconds).
    - max_queue (int/float): Maximum queue size (default: infinity).

    Returns:
    - times (list): Simulation time points.
    - queue_length (list): Queue length at each time point.
    """
    time = 0
    queue_length = []
    times = []
    arrival_time = 0
    departure_time = 0
    current_queue = 0

    while time < sim_time:
        # Generate random inter-arrival time (Poisson process)
        inter_arrival = random.expovariate(lambda_)
        arrival_time += inter_arrival
        time = arrival_time
        if time > sim_time:
            break

        # If queue is empty, start service immediately
        if current_queue == 0:
            service_time = random.expovariate(mu)
            departure_time = time + service_time
        else:
            # Continue serving next packet
            service_time = random.expovariate(mu)
            departure_time += service_time

        # Update queue based on arrival and departure
        if departure_time > time:
            current_queue += 1
            if current_queue > max_queue:
                current_queue = max_queue  # Drop packet if queue is full
        else:
            current_queue = max(0, current_queue - 1)

        times.append(time)
        queue_length.append(current_queue)

    return times, queue_length


if __name__ == "__main__":
    # Parameters: λ=0.8 pkt/s, μ=1.0 pkt/s, simulate for 100 seconds
    lambda_ = 0.8
    mu = 1.0
    times, queue_length = mm1_simulation(lambda_, mu)

    # Plot queue length over time
    plt.plot(times, queue_length)
    plt.xlabel("Time (seconds)")
    plt.ylabel("Queue Length (packets)")
    plt.title(f"M/M/1 Queue Simulation (λ={lambda_}, μ={mu})")
    plt.grid(True)
    plt.show()

    # Calculate and print average queue length
    avg_lq = np.mean(queue_length)
    print(f"Average Queue Length (L_q): {avg_lq:.2f} packets")
    # Compare with theoretical L_q = ρ² / (1 - ρ), where ρ = λ / μ
    rho = lambda_ / mu
    theoretical_lq = rho**2 / (1 - rho)
    print(f"Theoretical L_q: {theoretical_lq:.2f} packets")
