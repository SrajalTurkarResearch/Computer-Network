# wfq_simulation.py
# A standalone script to simulate Weighted Fair Queuing (WFQ) for QoS.
# Models multiple flows with weights, inspired by Tesla's flow orchestration.
# Requires: numpy

import numpy as np


class Packet:
    def __init__(self, arrival, size, flow):
        """
        Packet object for WFQ simulation.

        Parameters:
        - arrival (float): Arrival time (seconds).
        - size (int): Packet size (bits).
        - flow (int): Flow identifier.
        """
        self.arrival = arrival
        self.size = size
        self.flow = flow
        self.finish = 0  # Will be set by WFQ


def wfq_simulation(flow_weights, packets, link_rate):
    """
    Simulate WFQ scheduling for multiple flows.

    Parameters:
    - flow_weights (dict): Flow ID to weight (e.g., {1: 3, 2: 1}).
    - packets (list): List of Packet objects.
    - link_rate (float): Link speed (bits per second).

    Returns:
    - departures (list): Departure times of packets.
    """
    virtual_time = 0
    departures = []
    total_weight = sum(flow_weights.values())

    # Sort packets by arrival time
    for packet in sorted(packets, key=lambda x: x.arrival):
        # Calculate virtual finish time: F = max(previous F, arrival) + size / (rate * share)
        start = max(virtual_time, packet.arrival)
        share = flow_weights[packet.flow] / total_weight
        packet.finish = start + packet.size / (link_rate * share)
        virtual_time = packet.finish
        departures.append(packet.finish)

    return departures


if __name__ == "__main__":
    # Example: Two flows, link rate 10 Mbps
    flow_weights = {1: 3, 2: 1}  # Flow 1: video (weight 3), Flow 2: data (weight 1)
    packets = [
        Packet(arrival=0, size=12000, flow=1),  # 1500-byte video packet
        Packet(arrival=0, size=8000, flow=2),  # 1000-byte data packet
    ]
    link_rate = 10e6  # 10 Mbps

    # Run simulation
    departure_times = wfq_simulation(flow_weights, packets, link_rate)

    # Print results
    print("WFQ Simulation Results:")
    for i, (packet, dep_time) in enumerate(zip(packets, departure_times)):
        print(
            f"Packet {i+1}: Flow {packet.flow}, Size {packet.size} bits, Departure Time {dep_time:.6f} seconds"
        )
    # Flow 1 gets 75% bandwidth (3/4), Flow 2 gets 25% (1/4)
