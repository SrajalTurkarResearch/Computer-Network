# traffic_engineering.py
# Solves a simple SDN traffic engineering problem using PuLP to minimize max link load (lambda).
# Purpose: Demonstrate mathematical optimization for network traffic, key for SDN research.
# Requirements: Install PuLP (`pip install pulp`).
# Usage: Run directly with Python (`python traffic_engineering.py`).

from pulp import *

# Define the traffic engineering problem
prob = LpProblem("Traffic_Engineering", LpMinimize)

# Variables
lambda_var = LpVariable("lambda")  # Max link load
x = LpVariable("flow", 0)  # Flow on path S1->S2->S3

# Objective: Minimize lambda
prob += lambda_var

# Constraints
# We need to send 5 Mbps from S1 to S3 through S1->S2->S3
prob += x == 5  # Demand: 5 Mbps
prob += x <= 10 * lambda_var  # S1->S2 capacity (10 Mbps)
prob += x <= 10 * lambda_var  # S2->S3 capacity (10 Mbps)

# Solve the problem
prob.solve()

# Print results
print(f"Optimal lambda: {value(lambda_var):.2f}")  # Expected: 0.50 (50% link usage)

# For research: Extend this to multiple paths or flows for complex SDN scenarios.
# Example: Add a second path (S1->S3) and balance load.
