# data_center_load_balancing.py
# Simulates SDN-based load balancing in a data center, optimizing traffic across multiple paths.
# Purpose: Demonstrate how SDN optimizes data center traffic, inspired by Google's B4 network.
# Requirements: Install PuLP, NetworkX, Matplotlib (`pip install pulp networkx matplotlib`).
# Usage: Run directly (`python data_center_load_balancing.py`) to compute and visualize load balancing.

import pulp
import networkx as nx
import matplotlib.pyplot as plt

# Define the data center network as a graph
G = nx.Graph()
G.add_edges_from(
    [
        ("S1", "S2", {"capacity": 10}),
        ("S2", "S3", {"capacity": 10}),
        ("S1", "S3", {"capacity": 15}),
    ]
)  # Capacities in Mbps

# Traffic engineering problem: Minimize max link load (lambda)
prob = pulp.LpProblem("Data_Center_Load_Balancing", pulp.LpMinimize)
lambda_var = pulp.LpVariable("lambda")  # Max link load
x1 = pulp.LpVariable("path1", 0)  # Flow on S1->S2->S3
x2 = pulp.LpVariable("path2", 0)  # Flow on S1->S3

# Objective: Minimize lambda
prob += lambda_var

# Constraints: Send 12 Mbps from S1 to S3
prob += x1 + x2 == 12  # Total demand
prob += x1 <= 10 * lambda_var  # S1->S2 capacity
prob += x1 <= 10 * lambda_var  # S2->S3 capacity
prob += x2 <= 15 * lambda_var  # S1->S3 capacity

# Solve
prob.solve()
print(f"Optimal lambda: {pulp.value(lambda_var):.2f}")
print(f"Path S1->S2->S3: {pulp.value(x1):.2f} Mbps")
print(f"Path S1->S3: {pulp.value(x2):.2f} Mbps")

# Visualize the topology
plt.figure(figsize=(8, 6))
pos = nx.spring_layout(G)
nx.draw(G, pos, with_labels=True, node_color="lightblue", node_size=500, font_size=12)
edge_labels = {(u, v): f"{G[u][v]['capacity']} Mbps" for u, v in G.edges()}
nx.draw_network_edges(G, pos)
nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)
plt.title("Data Center SDN Topology")
plt.show()

# Notes for scientists:
# - Real-world impact: Google's B4 reduced latency by 30-50%.
# - Research idea: Extend to dynamic load balancing with real-time traffic data.
# - Try in Mininet: Simulate this topology and test with `iperf`.
