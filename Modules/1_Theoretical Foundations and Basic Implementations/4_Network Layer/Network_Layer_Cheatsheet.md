# Network Layer Cheatsheet

This cheatsheet summarizes key concepts, formulas, code snippets, and research tips for the Network Layer (IP Addressing, Forwarding, Routing Algorithms). Designed for beginners and aspiring scientists, it’s a quick reference for your notes and research journey. Use it alongside the Jupyter Notebook and case studies.

---

## 1. Network Layer Overview

- **Role** : Delivers packets across networks (OSI Layer 3).
- **Protocol** : Internet Protocol (IP) – connectionless, best-effort delivery.
- **Functions** :
- **IP Addressing** : Unique device IDs.
- **Forwarding** : Hop-by-hop packet decisions.
- **Routing** : Path computation (e.g., Dijkstra’s, Bellman-Ford).
- **Analogy** : Postal system – addresses (IP), local post offices (forwarding), route planning (routing).
- **Key Takeaway** : Scales internet to billions of devices.

---

## 2. IP Addressing

- **IPv4** : 32-bit, e.g., `192.168.1.1` (4.3B addresses).
- Format: `a.b.c.d` (0–255 per octet).
- Binary: `11000000.10101000.00000001.00000001`.
- **IPv6** : 128-bit, e.g., `2001:0db8::8a2e:0370:7334` (340 undecillion).
- Shorten: Omit leading zeros, collapse `::`.
- **Subnetting** : Split network (e.g., `192.168.1.0/24` → `/25`).
- **Special Addresses** :
- `127.0.0.1`: Localhost.
- `0.0.0.0`: Any.
- Private: `10.0.0.0/8`, `192.168.0.0/16`.
- **NAT** : Maps private to public IPs.
- **DHCP** : Auto-assigns IPs.

  **Formulas** :

- Hosts: `2^(32-mask) - 2` (e.g., /24 → 254 hosts).
- Network ID: `IP & Mask` (e.g., `192.168.1.5 & 255.255.255.0 = 192.168.1.0`).

  **Code Snippet** :

```python
def ip_to_binary(ip):
    return '.'.join(format(int(o), '08b') for o in ip.split('.'))
```

**Research Tip** : Explore IPv6 for IoT scalability or quantum addressing schemes.

---

## 3. Forwarding

- **Role** : Local hop decision at routers using forwarding tables.
- **Longest Prefix Match** : Most specific prefix (e.g., `/24` over `/16`).
- **Table Example** :

```
  | Prefix         | Next Hop     | Interface |
  |----------------|--------------|-----------|
  | 192.168.1.0/24 | Direct       | eth0      |
  | 0.0.0.0/0      | 192.168.1.1  | wan       |
```

- **Analogy** : Relay race – pass packet based on local map.
- **Key Takeaway** : Decentralized, scalable via prefix matching.

  **Code Snippet** :

```python
def longest_prefix_match(ip, table):
    # Implement prefix matching logic
    pass
```

**Research Tip** : Study SDN for programmable forwarding tables.

---

## 4. Routing Algorithms

- **Dijkstra’s (Link-State, OSPF)** :
- Global graph, non-negative weights.
- Greedy: Pick shortest unvisited path.
- Complexity: `O((|V| + |E|) log |V|)`.

  **Bellman-Ford (Distance-Vector, RIP)** :

- Decentralized, handles negative weights.
- Relaxation: `dist[v] = min(dist[v], dist[u] + w(u,v))`.
- Complexity: `O(|V|·|E|)`.
- Issue: Count-to-infinity (mitigate with split horizon).

  **Graph Example** :

```
A --1--> B --1--> C
 \
  5
   \--> C
```

**Code Snippet** (Dijkstra’s):

```python
import heapq
def dijkstra(graph, source):
    dist = {node: float('inf') for node in graph}
    dist[source] = 0
    pq = [(0, source)]
    while pq:
        d, u = heapq.heappop(pq)
        if d > dist[u]:
            continue
        for v, weight in graph[u].items():
            if dist[u] + weight < dist[v]:
                dist[v] = dist[u] + weight
                heapq.heappush(pq, (dist[v], v))
    return dist
```

**Research Tip** : Combine AI with routing for dynamic optimization.

---

## 5. Advanced Concepts

- **Fragmentation** :
- IPv4: Routers fragment if packet > MTU.
- IPv6: Sender fragments, simpler headers.
- **ICMP** : Errors (e.g., ping, traceroute).
- **Security** :
- IP Spoofing: Mitigate with ingress filtering.
- IPSec: Secure packet transfer.
- **QoS** : Prioritize traffic (e.g., DSCP field).

  **Research Tip** : Explore quantum routing for entanglement-based paths.

---

## 6. Visualizations

- **IP Space Plot** :

```python
  import matplotlib.pyplot as plt
  plt.bar(['IPv4', 'IPv6'], [2**32, 2**128], log=True)
  plt.ylabel('Addresses (log scale)')
  plt.show()
```

- **Network Graph** :

```python
  import networkx as nx
  G = nx.Graph()
  G.add_edge('A', 'B', weight=1)
  nx.draw(G, with_labels=True)
  plt.show()
```

---

## 7. Exercises

1. Convert `172.16.1.1` to binary.
2. Calculate hosts in `10.0.0.0/20`.
3. Run Dijkstra’s on graph: A-B=2, A-C=4, B-D=3, C-D=1.
4. Simulate Bellman-Ford with a negative weight edge.

**Solutions** :

- Q1: `10101100.00010000.00000001.00000001`.
- Q2: `2^(32-20) - 2 = 4094`.

---

## 8. Research Directions

- **AI Routing** : Optimize paths dynamically.
- **Quantum Networks** : Entanglement-based routing.
- **Interdisciplinary** : Apply routing to neural networks or logistics.
- **Simulation Tools** : NS-3, OMNeT++ for experiments.

---

## 9. What’s Missing in Standard Tutorials

- **Proofs** : Dijkstra’s correctness via induction.
- **Ethics** : Privacy risks of IP spoofing.
- **Interdisciplinary** : Routing in biological systems.
- **Future Protocols** : Quantum, DTN for space.

---

## 10. Next Steps

- **Learn** : SDN, QUIC, BGP.
- **Simulate** : Use Packet Tracer, GNS3.
- **Read** : Papers on AI routing, quantum networks.
- **Contribute** : Open-source (NetworkX, Scapy).

---

**Analogy Recap** : Network Layer = Postal system. IPs label envelopes, forwarding passes them, routing plans paths. Keep experimenting like a scientist!
