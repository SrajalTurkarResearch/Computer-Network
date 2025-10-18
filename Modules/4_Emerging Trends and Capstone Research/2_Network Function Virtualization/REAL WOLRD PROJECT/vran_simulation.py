# This script simulates a virtualized Radio Access Network (vRAN), inspired by Verizon’s 2025 deployment of 15,000+ virtualized 5G sites, which saved 35% energy by dynamically allocating resources. It models a virtual base station adjusting CPU allocation based on user demand, demonstrating NFV’s scalability and green benefits


# vran_simulation.py
# Purpose: Simulate a virtualized Radio Access Network (vRAN) for 5G, inspired by Verizon's 2025
# deployment using NFV to virtualize base stations, saving 35% energy. This script models a
# virtual base station dynamically allocating CPU units to handle user traffic, showcasing NFV's
# scalability and green benefits.
# Context: In NFV, vRAN replaces physical base stations with software (VNFs) on servers, allowing
# dynamic resource allocation. This is critical for 5G’s high demand and low latency.
# Dependencies: Install numpy, matplotlib (`pip install numpy matplotlib`).
# Math: Allocate CPU based on traffic demand D(t) = D_0 * sin(2πt) + base, ensuring capacity
# meets demand while minimizing energy (proportional to CPU used).
# For your scientist journey: This demonstrates dynamic resource management, key for 6G research.

import numpy as np
import matplotlib.pyplot as plt

# Step 1: Define simulation parameters
# Time: Simulate 24 hours (1 day).
time = np.linspace(0, 1, 24)  # 24 points from 0 to 1 (normalized time)
base_demand = 10  # Base traffic demand (CPU units)
peak_demand = 20  # Peak additional demand (e.g., during busy hours)
max_cpu = 40  # Server capacity (CPU units)
energy_per_cpu = 0.1  # Energy cost per CPU unit (kWh)

# Step 2: Model traffic demand
# Use a sine wave to simulate fluctuating user traffic (e.g., higher in evenings).
demand = base_demand + peak_demand * np.sin(2 * np.pi * time)

# Step 3: Allocate CPU dynamically
# Rule: Allocate enough CPU to meet demand, but not more than max_cpu.
# Add a safety margin (20%) to handle bursts.
allocated_cpu = np.minimum(demand * 1.2, max_cpu)
# Round up to nearest integer (CPU units are discrete).
allocated_cpu = np.ceil(allocated_cpu)

# Step 4: Calculate energy consumption
# Energy = CPU units used * energy per unit.
energy = allocated_cpu * energy_per_cpu
total_energy = np.sum(energy)
# Compare to static allocation (always use max_cpu).
static_energy = max_cpu * energy_per_cpu * len(time)

# Step 5: Print results
print("vRAN Simulation Results:")
print(f"Total Energy Used (Dynamic): {total_energy:.2f} kWh")
print(f"Total Energy Used (Static): {static_energy:.2f} kWh")
print(f"Energy Savings: {(static_energy - total_energy) / static_energy * 100:.2f}%")

# Step 6: Visualize demand vs. allocation
plt.plot(time, demand, label="Traffic Demand", color="blue")
plt.plot(time, allocated_cpu, label="Allocated CPU", color="green", linestyle="--")
plt.axhline(max_cpu, color="red", linestyle=":", label="Max CPU")
plt.xlabel("Time (Normalized, 1 = 24 hours)")
plt.ylabel("CPU Units")
plt.title("vRAN Dynamic CPU Allocation")
plt.legend()
plt.grid(True)
plt.show()

# Explanation:
# - Blue line: Traffic demand fluctuates (e.g., peaks at busy hours).
# - Green dashed line: CPU allocated dynamically to meet demand + 20% margin.
# - Red dotted line: Max server capacity (40 units).
# - Energy savings: Dynamic allocation uses less CPU than static, saving energy.

# For Your Research:
# - Modify `peak_demand` to simulate higher traffic (e.g., 50 units).
# - Add multiple servers and optimize allocation (use vnf_placement.py logic).
# - Research Question: How can vRAN optimize for 6G ultra-low latency (<0.1ms)?
# - Publish a plot comparing energy savings in a conference paper.
