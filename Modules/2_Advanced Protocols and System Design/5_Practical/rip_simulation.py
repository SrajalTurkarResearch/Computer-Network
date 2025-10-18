# rip_simulation.py
"""
Tutorial File 2: Simulating RIP Routing with Hop Count
Purpose: Understand RIP (Routing Information Protocol), a distance vector protocol that picks paths with fewest hops.
This script simulates choosing the shortest path by hop count and includes a mini-project.
For aspiring scientists: Modify the paths to study convergence time.
"""


# Simulate RIP’s hop-count-based routing
def rip_hop_count(paths):
    """
    Choose the path with the fewest hops (like RIP).
    paths: List of possible paths (e.g., [['R1', 'R2', 'R3'], ['R1', 'R4', 'R3']])
    Returns: Path with minimum hops
    """
    return min(paths, key=len)


# Sample paths in a network
paths = [
    ["R1", "R2", "R3"],  # 3 nodes = 2 hops
    ["R1", "R4", "R3", "R5"],  # 4 nodes = 3 hops
]

# Run RIP simulation
best_path = rip_hop_count(paths)
print("RIP chooses shortest path (fewest hops):", best_path)
# Example output: ['R1', 'R2', 'R3'] (2 hops)

# Mini-Project: Compare RIP paths under failure
"""
Mini-Project: Simulate RIP convergence
1. Add a new path: ['R1', 'R5', 'R3']
2. Simulate a link failure (remove ['R1', 'R2', 'R3'])
3. Rerun rip_hop_count to see new choice
"""
new_paths = [
    ["R1", "R5", "R3"],  # New path: 2 hops
    ["R1", "R4", "R3", "R5"],  # Old path: 3 hops
]
print("After link failure, RIP chooses:", rip_hop_count(new_paths))

# For Scientists: Research Idea
"""
RIP has slow convergence (up to 180 seconds). Experiment with:
- Adding more paths to see how RIP handles complexity.
- Compare with EIGRP (faster convergence, per 2024 studies).
- Use CAIDA dataset[](https://www.caida.org) for real-world path analysis.
"""
