# Cheatsheet for Routing Protocols, Network Performance Optimization, and Simulation

This cheatsheet summarizes the tutorial on computer networks in a simple, note-friendly format. It covers key concepts, commands, formulas, and research ideas to help you master routing protocols, optimization, and simulation as an aspiring scientist. Use it as a quick reference while studying or experimenting!

---

## 1. Key Concepts

- **Computer Network** : Devices (nodes) connected by links (wires/Wi-Fi) to share data, like a city with roads.
- **Routing** : Finding the best path for data, like a postal service picking delivery routes.
- **Routing Protocols** :
- **Distance Vector (e.g., RIP)** : Picks paths with fewest stops (hops).
- **Link-State (e.g., OSPF)** : Picks fastest paths using a full network map.
- **Path Vector (e.g., BGP)** : Picks paths across big networks (like Internet providers).
- **Optimization** : Making networks faster (low delay, high speed).
- **Simulation** : Testing networks virtually, like a video game city.
- **Key Terms** :
- **Routing Table** : List of paths (e.g., “To Network A, go via Router B, 2 hops”).
- **Metric** : Number to compare paths (e.g., hops, bandwidth).
- **Convergence** : When routers agree on paths after a change (faster = better).

---

## 2. Routing Protocols

- **RIP (Routing Information Protocol)** :
- How: Shares routing tables every 30 seconds, picks fewest hops (max 15).
- Use: Small networks (e.g., school).
- Math: Bellman-Ford (find shortest path by asking neighbors).
- **OSPF (Open Shortest Path First)** :
- How: Builds full map, picks fastest paths based on bandwidth.
- Use: Big networks (e.g., university).
- Math: Dijkstra’s algorithm (add up road costs).
- **BGP (Border Gateway Protocol)** :
- How: Lists networks (ASes) to cross, picks based on rules.
- Use: Internet (e.g., between AT&T and Google).
- **Static vs. Dynamic** :
- Static: Manual paths, simple but rigid.
- Dynamic: Automatic paths (RIP, OSPF), adapts to changes.

---

## 3. Practical Commands (Cisco Packet Tracer)

- **RIP Setup (on Router R1)** :

```bash
  R1> enable
  R1# configure terminal
  R1(config)# router rip
  R1(config-router)# version 2
  R1(config-router)# network 192.168.1.0
  R1(config-router)# network 192.168.5.0
```

- **OSPF Setup (on Router R1)** :

```bash
  R1> enable
  R1# configure terminal
  R1(config)# router ospf 1
  R1(config-router)# network 192.168.1.0 0.0.0.255 area 0
```

- **BGP Setup (on Router R1, AS 100)** :

```bash
  R1> enable
  R1# configure terminal
  R1(config)# router bgp 100
  R1(config-router)# neighbor 192.168.4.2 remote-as 200
```

---

## 4. Optimization Techniques

- **Quality of Service (QoS)** : Prioritize important data (e.g., video over email).
- **Load Balancing** : Split traffic across multiple paths.
- **Compression** : Shrink data for faster travel.
- **Caching** : Store data nearby (e.g., Netflix servers).
- **Traffic Engineering** : Plan paths to avoid traffic jams (e.g., MPLS).

---

## 5. Key Math Formulas

- **M/M/1 Queuing Model** :
- Waiting Time: ( W = \frac{1}{\mu - \lambda} )
  - ( \lambda ): Arrival rate (packets/s).
  - ( \mu ): Service rate (packets processed/s).
- Queue Length: ( L = \lambda \cdot W ) (Little’s Law).
- Example: ( \lambda = 50 ), ( \mu = 100 ), then ( W = \frac{1}{100 - 50} = 0.02 ) s, ( L = 50 \cdot 0.02 = 1 ) packet.
- **Dijkstra’s Algorithm (OSPF)** :
- Total Cost = Sum of link costs (e.g., ( \frac{10^8}{\text{bandwidth}} )).
- **Bellman-Ford (RIP)** :
- Distance = Min(Neighbor’s distance + Link cost).

---

## 6. Simulation Tools

- **Packet Tracer** : Free, drag-and-drop, beginner-friendly (Cisco).
- **NS-3** : Free, code-based for research (Linux/WSL).
- **OMNeT++** : Free, detailed simulations.
- **GNS3** : Free, realistic router emulation.

---

## 7. Research Ideas

- **Software-Defined Networking (SDN)** : Control routers centrally for smarter routing.
- **AI Routing** : Use AI to predict traffic (e.g., RouteNet-Fermi, 2025).
- **Energy-Efficient Protocols** : Save battery in IoT devices (e.g., 2024 fuzzy cuckoo search).
- **Quantum Networking** : Use quantum signals for secure, fast routing.

---

## 8. Quick Code Snippets (Python)

- **Dijkstra’s Algorithm (OSPF)** :

```python
  from heapq import heappush, heappop
  def dijkstra(graph, start):
      queue = [(0, start)]
      distances = {node: float('inf') for node in graph}
      distances[start] = 0
      while queue:
          d, node = heappop(queue)
          for neighbor, w in graph[node].items():
              if d + w < distances[neighbor]:
                  distances[neighbor] = d + w
                  heappush(queue, (d + w, neighbor))
      return distances
```

- **Visualize Network** :

```python
  import networkx as nx
  import matplotlib.pyplot as plt
  G = nx.Graph()
  G.add_edge('R1', 'R2', weight=1)
  nx.draw(G, with_labels=True)
  plt.show()
```

---

## 9. Common Issues and Fixes

- **RIP** : Slow convergence? Check hop limit (15) or update timers.
- **OSPF** : No routes? Ensure same area ID (e.g., Area 0).
- **BGP** : No connection? Verify AS numbers and IP reachability.

---

## 10. Datasets for Research

- **CAIDA** : Real Internet traffic data ([https://www.caida.org](https://www.caida.org/)).
- **GenNP** : Network performance dataset (2024).
- **UOS_IOTSH_2024** : IoT sensor network data.

---

## 11. Next Steps

- Practice: Build networks in Packet Tracer.
- Simulate: Use NS-3 for research-grade experiments.
- Research: Explore SDN, AI routing, or quantum networking.
- Read: “Computer Networking: A Top-Down Approach” by Kurose and Ross.
- Join: SIGCOMM for networking conferences.

This cheatsheet is your quick guide to mastering networks. Keep it handy for coding, simulating, and researching!
