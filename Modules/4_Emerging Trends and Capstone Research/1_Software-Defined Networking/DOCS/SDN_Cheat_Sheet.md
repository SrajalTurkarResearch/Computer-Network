# SDN Cheat Sheet: Your Quick Reference for Software-Defined Networking

This cheat sheet summarizes key concepts, tools, protocols, and commands from the SDN tutorial, designed for beginners aiming to become network scientists. Use it as a quick reference to master SDN theory and practice. All terms are explained clearly, with analogies to make them stick.

## 1. Core Concepts

- **Computer Network** : Devices (e.g., phones, servers) connected to share data via packets (small data chunks, like letters).
- **Analogy** : A town where people (devices) send letters (packets) via bikes (links).
- **Traditional Networking** :
- Each device (router/switch) has its own “brain” (firmware) with a **routing table** (map for packet paths).
- Problems: Hard to update, expensive, slow to scale, inflexible.
- **Software-Defined Networking (SDN)** :
- Separates **control plane** (decisions) from **data plane** (packet forwarding).
- Central **SDN controller** manages all switches via software.
- **Analogy** : A conductor (controller) leading an orchestra (switches) vs. musicians playing solo.
- **SDN Benefits** :
- Programmable: Change network behavior with code (e.g., Python).
- Flexible: Adapt to traffic spikes or attacks instantly.
- Cost-effective: Use cheap switches instead of pricey routers.

## 2. SDN Architecture

- **Data Plane** : Switches forward packets based on **flow tables** (rules like “if dst_IP = X, send to Port Y”).
- **Control Plane** : SDN controller computes paths and sends rules via **Southbound API** (e.g., OpenFlow).
- **Application Plane** : Apps (e.g., firewall, load balancer) request services via **Northbound API** .
- **Analogy** : Pizza delivery:
- Data Plane: Scooters (switches) delivering pizzas (packets).
- Control Plane: Manager (controller) assigning routes.
- Application Plane: Customers (apps) requesting fast delivery.

  **Sketch** : Draw 3 layers: Switches (bottom) → Controller (middle) → Apps (top). Label Southbound (OpenFlow) and Northbound (APIs).

## 3. Key Protocols and Tools

- **OpenFlow** :
- Language for controller-switch communication.
- Flow table format: **Match** (e.g., IP, port), **Action** (forward, drop), **Counter** (packet count).
- Example: “If dst_IP = 10.0.0.1, forward to Port 2.”
- **Controllers** :
- **Ryu** : Python-based, beginner-friendly (`pip install ryu`).
- **OpenDaylight** : Enterprise-grade, complex networks.
- **ONOS** : Reliable for 5G telecom.
- **Mininet** : Virtual network emulator (`sudo apt-get install mininet`).
- Example: `sudo mn --topo=linear,3` (3 switches, 3 hosts).
- **Wireshark** : Captures packets to analyze flows.
- **PuLP** : Python library for traffic optimization (`pip install pulp`).
- **NetworkX/Matplotlib** : Visualize topologies (`pip install networkx matplotlib`).

## 4. Essential Commands

- **Mininet** :
- Create a topology: `sudo mn --topo=tree,depth=2,fanout=2 --controller=remote`
- Test connectivity: `pingall`
- Simulate traffic: `iperf -u -p 8801` (UDP traffic)
- **Ryu** :
- Run controller: `ryu-manager simple_switch.py`
- **Wireshark** : Launch and filter for OpenFlow packets: `openflow_v4`

## 5. Key Math Concepts

- **Traffic Engineering** :
- Goal: Minimize max link load (λ).
- Model: Network as a graph, edges with capacity $c_e$, flows $x_p$.
- Objective: $\min \lambda$, s.t. $\sum_{p \text{ using } e} x_p \leq \lambda \cdot c_e$.
- Example: 5 Mbps demand, 10 Mbps links → $\lambda = 0.5$ (50% usage).
- **Entropy for Security** :
- Detect attacks (e.g., DDoS) with low entropy.
- Formula: $H = -\sum p_i \log_2 p_i$, where $p_i$ = fraction of packets from source $i$.
- Example: Normal (50, 30, 20 packets) → $H \approx 1.5$; Attack (90, 10) → $H \approx 0.47$.

## 6. Real-World Applications

- **Data Centers** : Google’s B4 uses SDN to balance traffic, cutting latency by 30–50%.
- **Telecom** : AT&T’s 5G allocates bandwidth dynamically with SDN.
- **Security** : SDN firewalls block threats instantly (e.g., 2023 hospital attack mitigation).
- **IoT/Smart Cities** : Singapore’s SDN manages traffic/pollution sensors, reducing congestion by 15%.

## 7. Quick Code Snippets

- **Ryu Controller (Basic)** :

```python
  match = parser.OFPMatch()
  actions = [parser.OFPActionOutput(ofproto.OFPP_CONTROLLER)]
  self.add_flow(datapath, 0, match, actions)
```

- **Prioritize UDP (Video)** :

```python
  match_udp = parser.OFPMatch(ip_proto=17, udp_dst=8801)
  actions = [parser.OFPActionOutput(ofproto.OFPP_NORMAL)]
  self.add_flow(datapath, 10, match_udp, actions)
```

- **Entropy Calculation** :

```python
  probs = [p/sum(packets) for p in packets]
  H = -sum(p * np.log2(p) for p in probs if p > 0)
```

## 8. Research Tips

- **Experiment** : Use Mininet to test load balancing or security rules.
- **Extend** : Add AI to predict traffic or quantum SDN for secure networks.
- **Read** : IEEE Xplore (“SDN applications”), RFC 7426 (SDN standards).
- **Project** : Simulate a lunar base network, addressing Earth-Mars delays.

## 9. Common Pitfalls

- **Controller Bottlenecks** : Handling millions of flows can overwhelm a single controller. Solution: Use distributed controllers (e.g., ONOS).
- **Security Risks** : Protect the controller with encryption.
- **Compatibility** : Mixing SDN with legacy networks is tricky; test in Mininet first.

  **Sketch** : Draw a flow table: Match (dst_IP = 10.0.0.1) → Action (Port 2) → Counter (100 packets).

  **Keep This Handy** : Print or save this cheat sheet for quick reference while coding or studying SDN. Your journey to network scientist starts here!
