"""
bgp_simulation.py
Simulates a BGP network with ASes and checks for routing loops.
Models basic AS connectivity and path vectors.
Requires: networkx
Run: python bgp_simulation.py
"""

import networkx as nx

# Create a directed graph for BGP simulation
bgp_graph = nx.DiGraph()
bgp_graph.add_edge("AS1", "AS2", as_path=[1, 2])
bgp_graph.add_edge("AS1", "AS3", as_path=[1, 3, 2])
# Add more edges for complex topology
bgp_graph.add_edge("AS3", "AS2", as_path=[3, 2])

# Check for routing loops (cycles in AS paths)
has_cycle = list(nx.simple_cycles(bgp_graph))
print(f"Has Routing Loops: {bool(has_cycle)}")
if has_cycle:
    print(f"Detected Cycles: {has_cycle}")

"""
Explanation:
- Models ASes as nodes and eBGP sessions as directed edges with AS-paths.
- Checks for cycles, which BGP prevents via AS-path loop detection.
- Simulates a small internet topology to test stability.
- Extend by parsing real BGP tables (e.g., from Routeviews).
"""
