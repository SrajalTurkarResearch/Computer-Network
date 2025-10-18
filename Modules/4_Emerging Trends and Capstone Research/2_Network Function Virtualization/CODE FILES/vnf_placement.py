# vnf_placement.py
# Purpose: Simulate Virtual Network Function (VNF) placement on servers using Integer Linear Programming (ILP).
# Context: In NFV, VNFs (e.g., virtual firewall, router) are software tasks placed on servers to minimize cost
# while respecting server capacity. This script models a small network with 3 VNFs and 2 servers.
# For your scientist journey, this demonstrates optimization, a key skill for network research.
# Dependencies: Install PuLP (`pip install pulp`).
# Math: Minimize cost = sum(server_cost * VNF_assignment), subject to:
#   1. Each VNF on exactly one server.
#   2. Server capacity not exceeded.

from pulp import *

# Step 1: Define the optimization problem
# We aim to minimize total server cost (like minimizing energy or hardware use).
prob = LpProblem("VNF_Placement", LpMinimize)

# Step 2: Define data
# VNFs: Each needs CPU units (e.g., Firewall needs 3 units).
vnfs = {"Firewall": 3, "IDS": 2, "LoadBalancer": 4}
# Servers: Each has capacity (CPU units) and cost (e.g., power usage).
servers = {"S1": {"cap": 5, "cost": 10}, "S2": {"cap": 6, "cost": 15}}

# Step 3: Create variables
# x[v,s] = 1 if VNF v is placed on server s, else 0 (binary variable).
x = LpVariable.dicts("x", [(v, s) for v in vnfs for s in servers], cat="Binary")

# Step 4: Set objective
# Minimize total cost: sum(cost of server s * whether server s is used).
prob += lpSum(servers[s]["cost"] * x[v, s] for v in vnfs for s in servers)

# Step 5: Add constraints
# Constraint 1: Each VNF must be placed on exactly one server.
for v in vnfs:
    prob += lpSum(x[v, s] for s in servers) == 1, f"One_server_{v}"
# Constraint 2: Server capacity cannot be exceeded.
for s in servers:
    prob += lpSum(vnfs[v] * x[v, s] for v in vnfs) <= servers[s]["cap"], f"Cap_{s}"

# Step 6: Solve the problem
# PuLP uses a solver (default: CBC) to find the optimal placement.
prob.solve()

# Step 7: Print results
print("Optimization Status:", LpStatus[prob.status])
print("Total Cost:", value(prob.objective))
for v in vnfs:
    for s in servers:
        if value(x[v, s]) == 1:
            print(f"{v} placed on {s}")

# Explanation of Output:
# - Status: "Optimal" means a solution was found.
# - Cost: Sum of server costs for used servers.
# - Placement: Shows which VNFs are on which servers.
# Example Output: Firewall and IDS on S1 (5 units total), LoadBalancer on S2, cost = 25.

# For Your Research:
# - Try changing VNF demands or server capacities.
# - Scale to 10 VNFs and 5 servers for a mini-project.
# - Explore heuristics (e.g., greedy placement) for large networks.
