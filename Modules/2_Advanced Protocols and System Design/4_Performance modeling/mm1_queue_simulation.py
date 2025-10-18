import random


def simulate_mm1_queue(lambda_rate=10, mu_rate=15, sim_time=1000):
    """
    Simulate M/M/1 queue with Poisson arrivals (rate lambda) and exponential service (rate mu).
    Computes average queuing delay using Little's Law.
    Parameters:
        lambda_rate: Arrival rate (packets/sec)
        mu_rate: Service rate (packets/sec)
        sim_time: Simulation duration (seconds)
    """
    queue = 0
    time = 0
    total_wait = 0
    packets = 0

    print(f"Simulating M/M/1 Queue: λ={lambda_rate}, μ={mu_rate}, Time={sim_time}s")

    while time < sim_time:
        # Time to next arrival or service
        arrival_time = random.expovariate(lambda_rate)
        service_time = random.expovariate(mu_rate) if queue > 0 else float("inf")

        if arrival_time < service_time:
            # New packet arrives
            queue += 1
            packets += 1
            time += arrival_time
        else:
            # Packet served
            queue -= 1
            total_wait += queue / lambda_rate  # Waiting time for packets in queue
            time += service_time

    avg_delay = total_wait / packets if packets > 0 else 0
    print(f"Average Queuing Delay: {avg_delay * 1000:.2f} ms")


if __name__ == "__main__":
    simulate_mm1_queue()
