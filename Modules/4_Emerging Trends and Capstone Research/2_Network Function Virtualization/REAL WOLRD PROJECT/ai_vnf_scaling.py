# This script simulates AI-driven scaling of VNFs, inspired by AT&T’s 2025 use of AI to predict traffic and scale VNFs dynamically. It implements a simplified Q-learning algorithm to decide when to add or remove VNF instances based on traffic load, demonstrating NFV’s agility and AI integration.


# ai_vnf_scaling.py
# Purpose: Simulate AI-driven VNF scaling, inspired by AT&T's 2025 use of AI to predict and
# scale VNFs (e.g., virtual firewalls) based on traffic. This script uses simplified Q-learning
# to decide how many VNF instances to run, balancing latency and cost.
# Context: In NFV, scaling VNFs dynamically ensures performance during traffic spikes while
# minimizing server use. AI predicts demand to optimize scaling.
# Dependencies: Install numpy, matplotlib (`pip install numpy matplotlib`).
# Math: Q-learning updates Q(s,a) = Q(s,a) + α[R + γ*max(Q(s',a')) - Q(s,a)], where R is
# reward based on latency and cost.
# For your scientist journey: This introduces reinforcement learning for network optimization.

import numpy as np
import matplotlib.pyplot as plt

# Step 1: Define simulation parameters
# Simulate 24 hours with fluctuating traffic.
time = np.linspace(0, 1, 24)
base_traffic = 50  # Base traffic (packets/s)
peak_traffic = 100  # Peak additional traffic
vnf_capacity = 80  # Max packets/s per VNF instance
cost_per_vnf = 5  # Cost per VNF instance (e.g., server resources)
latency_threshold = 0.05  # Target latency (seconds)
alpha = 0.1  # Learning rate for Q-learning
gamma = 0.9  # Discount factor

# Step 2: Model traffic
traffic = base_traffic + peak_traffic * np.sin(2 * np.pi * time)

# Step 3: Initialize Q-table
# States: Traffic levels (discretized into low, medium, high).
# Actions: Number of VNFs (1, 2, 3).
states = ["low", "med", "high"]  # Traffic <80, 80-160, >160
actions = [1, 2, 3]  # Number of VNF instances
Q = np.zeros((len(states), len(actions)))  # Q-table initialized to 0

# Step 4: Simulate Q-learning for scaling
num_vnfs = [1] * len(time)  # Start with 1 VNF
latencies = []
for t in range(len(time)):
    # Get state based on traffic
    if traffic[t] < 80:
        state = 0  # Low
    elif traffic[t] < 160:
        state = 1  # Medium
    else:
        state = 2  # High

    # Choose action (number of VNFs) with highest Q-value
    action = np.argmax(Q[state])
    num_vnfs[t] = actions[action]

    # Calculate latency (M/M/1 queue model, simplified)
    total_capacity = num_vnfs[t] * vnf_capacity
    latency = 1 / (total_capacity - traffic[t]) if total_capacity > traffic[t] else 0.1
    latencies.append(latency)

    # Calculate reward: High if latency < threshold, low if over; penalize cost
    reward = 10 if latency < latency_threshold else -10
    reward -= cost_per_vnf * num_vnfs[t]

    # Update Q-table
    next_state = state  # Simplified: Assume state doesn’t change instantly
    Q[state, action] += alpha * (
        reward + gamma * np.max(Q[next_state]) - Q[state, action]
    )

# Step 5: Print results
print("AI-Driven VNF Scaling Results:")
print(f"Average Latency: {np.mean(latencies):.3f} seconds")
print(f"Average VNFs Used: {np.mean(num_vnfs):.2f}")
print(f"Total Cost: {np.sum(num_vnfs) * cost_per_vnf:.2f}")

# Step 6: Visualize traffic vs. VNFs
plt.plot(time, traffic, label="Traffic (packets/s)", color="blue")
plt.plot(
    time,
    [n * vnf_capacity for n in num_vnfs],
    label="VNF Capacity",
    color="green",
    linestyle="--",
)
plt.xlabel("Time (Normalized, 1 = 24 hours)")
plt.ylabel("Packets/s")
plt.title("AI-Driven VNF Scaling")
plt.legend()
plt.grid(True)
plt.show()

# Explanation:
# - Blue line: Traffic fluctuates, peaking at busy hours.
# - Green dashed line: Total capacity from VNFs, adjusted by Q-learning.
# - Q-learning learns to add VNFs when traffic is high, balancing latency and cost.

# For Your Research:
# - Adjust `alpha` or `gamma` to tune learning speed.
# - Add more states (e.g., finer traffic bins) or actions (e.g., 4 VNFs).
# - Research Question: Can deep Q-learning improve scaling for 6G?
# - Publish a comparison of AI vs. static scaling in a journal.
