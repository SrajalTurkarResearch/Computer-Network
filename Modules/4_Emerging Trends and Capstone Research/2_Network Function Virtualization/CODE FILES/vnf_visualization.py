# vnf_visualization.py
# Purpose: Visualize server utilization after VNF placement to understand resource allocation.
# Context: In NFV, after placing VNFs (e.g., Firewall, IDS) on servers, we want to see how much
# server capacity is used vs. available. This helps optimize network design.
# Dependencies: Install Matplotlib (`pip install matplotlib`).
# For your scientist journey, visualizations are key to communicating research findings.

import matplotlib.pyplot as plt

# Step 1: Define data from VNF placement
# Based on vnf_placement.py output: Firewall+IDS (5 units) on S1, LoadBalancer (4 units) on S2.
servers = ["S1", "S2"]
capacities = [5, 6]  # Total CPU units available per server
used = [5, 4]  # CPU units used (from optimization result)

# Step 2: Create bar plot
# Plot total capacity (light blue) and used capacity (darker blue) for each server.
plt.bar(servers, capacities, alpha=0.5, label="Total Capacity", color="lightblue")
plt.bar(servers, used, alpha=0.8, label="Used Capacity", color="blue")

# Step 3: Customize plot
plt.xlabel("Servers")
plt.ylabel("CPU Units")
plt.title("Server Utilization in NFV Placement")
plt.legend()

# Step 4: Display plot
plt.show()

# Explanation:
# - Light blue bars show total server capacity (S1: 5 units, S2: 6 units).
# - Dark blue bars show used capacity (S1: 5 units, S2: 4 units).
# - This visual confirms S1 is fully used, S2 has spare capacity.

# For Your Research:
# - Modify `used` to reflect different placement scenarios.
# - Add more servers or metrics (e.g., memory usage).
# - Publish this plot in a research paper to show optimization results.
