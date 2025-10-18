"""
bgp_path_selection.py
Simulates BGP path selection for a given prefix based on attributes.
Chooses the best path using Local Preference and AS-Path length.
Run: python bgp_path_selection.py
"""

# Sample BGP paths for prefix 8.8.8.0/24 (e.g., Google DNS)
paths = [
    {"prefix": "8.8.8.0/24", "as_path": [15169], "local_pref": 100},  # Direct to Google
    {"prefix": "8.8.8.0/24", "as_path": [701, 15169], "local_pref": 50},  # Via Verizon
]

# Select best path: Highest local_pref, then shortest AS-path
best_path = max(paths, key=lambda p: (p["local_pref"], -len(p["as_path"])))
print(
    f"Best BGP Path: AS-Path {best_path['as_path']}, Local Preference {best_path['local_pref']}"
)

"""
Explanation:
- Each path has a prefix, AS-Path (list of ASes), and Local Preference.
- Lambda function prioritizes higher Local Preference, then shorter AS-Path.
- Simulates BGP's decision process in choosing routes between ASes.
- Example output: Prefers direct path to AS15169 due to higher local_pref.
"""
