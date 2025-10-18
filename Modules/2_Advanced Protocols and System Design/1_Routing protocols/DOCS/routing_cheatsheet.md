# Routing Protocols Cheatsheet: OSPF, BGP, and Convergence

This cheatsheet is your quick guide to mastering OSPF, BGP, and routing convergence, tailored for aspiring network scientists. It summarizes key concepts, commands, and tips from the tutorial, addressing gaps in standard resources (e.g., protocol interactions, security, formal proofs). Use it for study, practice, or research planning.

## 1. Core Concepts

- **Computer Network** : Devices (nodes) connected by links to share data packets.
- **Nodes** : Routers, servers, phones.
- **Links** : Cables (Ethernet), wireless (Wi-Fi).
- **Packets** : Data chunks with source/destination IPs.
- **Routing** : Finding the best path for packets using routing tables.
- **Static** : Manual paths (e.g., home router to printer).
- **Dynamic** : Protocols like OSPF (inside orgs), BGP (between orgs).
- **Graph Theory** : Networks as graphs (G = (V, E)).
- V = routers, E = links with costs (e.g., delay).
- Goal: Find shortest paths (lowest cost).

  **Draw This** : Sketch 3 routers (R1, R2, R3) with links (R1-R2=10, R1-R3=15, R2-R3=5).

## 2. OSPF (Open Shortest Path First)

- **Type** : Interior Gateway Protocol (IGP), link-state.
- **Where Used** : Inside organizations (e.g., company networks).
- **How It Works** :
- Routers share Link-State Advertisements (LSAs) to build a map (Link-State Database, LSDB).
- Use Dijkstra’s algorithm to find shortest paths.
- Areas (e.g., Area 0) split large networks.
- Fast convergence (~0.5s).
- **Key Terms** :
- **LSA** : Message about links (e.g., “R1 to R2, cost=10”).
- **LSDB** : Shared network map.
- **Cost** : Link metric (e.g., 100Mbps/LinkSpeed).
- **DR** : Designated Router to reduce chatter in busy networks.
- **Pros** : Fast, loop-free, scalable with areas.
- **Cons** : High CPU/memory for large LSDBs.

  **Cisco Config** :

```bash
router ospf 1
 network 192.168.1.0 0.0.0.255 area 0
 interface GigabitEthernet0/0
  ip ospf cost 10
```

**Python (Dijkstra)** :

```python
import networkx as nx
G = nx.Graph()
G.add_edge('R1', 'R2', weight=10)
path = nx.dijkstra_path(G, 'R1', 'R3', weight='weight')
```

**Tip** : Use Packet Tracer to simulate OSPF; try breaking a link.

## 3. BGP (Border Gateway Protocol)

- **Type** : Exterior Gateway Protocol (EGP), path-vector.
- **Where Used** : Between organizations (e.g., ISPs, Google).
- **How It Works** :
- Routers share paths (AS-Path) for prefixes (e.g., 8.8.8.0/24).
- Pick best path by attributes: Local Preference > AS-Path length > MED.
- eBGP (between ASes), iBGP (within AS).
- Slower convergence (10-60s).
- **Key Terms** :
- **AS** : Autonomous System (e.g., AS15169 = Google).
- **Prefix** : IP range (e.g., 8.8.8.0/24).
- **Attributes** : LocalPref (priority), AS-Path (hops), MED (path preference).
- **Pros** : Scales to internet size, policy-driven.
- **Cons** : Slow, vulnerable to hijacks.

  **Cisco Config** :

```bash
router bgp 65001
 neighbor 192.168.1.2 remote-as 65002
 network 10.0.0.0 mask 255.255.0.0
```

**Python (Path Selection)** :

```python
paths = [{'prefix': '8.8.8.0/24', 'as_path': [15169], 'local_pref': 100}]
best = max(paths, key=lambda p: (p['local_pref'], -len(p['as_path'])))
```

**Tip** : Use GNS3 for BGP; check Routeviews for real BGP data.

## 4. Convergence

- **Definition** : Time for routers to agree on paths after a change (e.g., link failure).
- **OSPF** : Fast (~0.5s) via LSA flooding and Dijkstra.
- **BGP** : Slower (10-60s) due to AS-by-AS updates.
- **Proofs** :
- OSPF: LSDB sync + Dijkstra → loop-free tree (□◇Stable).
- BGP: AS-Path loop check + valley-free policies → finite convergence.

  **Plot Convergence** :

```python
import numpy as np, matplotlib.pyplot as plt
sizes = np.arange(10, 100, 10)
plt.plot(sizes, sizes * np.log(sizes) / 1000, label='OSPF')
plt.plot(sizes, sizes**3 / 1e6, label='BGP')
plt.legend()
plt.show()
```

## 5. Security Tips

- **OSPF** :
- Issue: Fake LSAs can disrupt routing.
- Fix: Use MD5 authentication (`ip ospf authentication`).
- **BGP** :
- Issue: Hijacks (e.g., 2008 YouTube).
- Fix: RPKI for prefix validation, BGPsec for path authentication.

## 6. Research Ideas

- **AI** : Predict BGP hijacks or optimize OSPF areas.
- **Quantum** : Design quantum-safe BGP.
- **Verification** : Use TLA+/Coq to prove protocol correctness.

## 7. Gaps in Standard Tutorials

- **Missed Topics** : BGP-OSPF interactions, convergence proofs, RPKI flaws.
- **This Cheatsheet Adds** : Quick configs, code snippets, research prompts.

## 8. Quick Tools

- **Simulators** : Packet Tracer (OSPF), GNS3 (BGP), ns-3 (advanced).
- **Data** : Routeviews (BGP tables), RIPEstat (prefix stats).
- **Verification** : TLA+, Coq for proofs.

## 9. Next Steps

- Read RFC 2328 (OSPF), RFC 4271 (BGP).
- Simulate networks in GNS3; code Dijkstra in Python.
- Explore AI routing or quantum protocols for research.

  **Motivation** : You’re on the path to inventing the networks of 2050, like Tesla building AC power!
