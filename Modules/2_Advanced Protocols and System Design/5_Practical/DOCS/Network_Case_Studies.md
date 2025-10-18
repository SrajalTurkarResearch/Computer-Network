# Case Studies in Routing Protocols, Network Performance Optimization, and Simulation

This file presents detailed case studies to complement your tutorial on computer networks. Each case study showcases real-world applications or recent research (as of 2025), explaining how routing protocols, optimization techniques, and simulations are used in practice. Written in simple language, these cases are designed for aspiring scientists to understand, take notes, and draw inspiration for research. Each includes context, technical details, outcomes, and ideas for further exploration.

---

## Case Study 1: Optimizing a Corporate Network with OPNET Simulation

### Context

A large company with offices in multiple cities faced slow file transfers and video call dropouts due to inefficient routing. They used **OPNET** (now Riverbed Modeler), a network simulation tool, to test RIP (Routing Information Protocol) versus EIGRP (Enhanced Interior Gateway Routing Protocol) for their corporate network.

### Technical Details

- **Network Setup** : 10 routers connecting 5 offices, each with a LAN (Local Area Network).
- **Simulation** : OPNET modeled the network with realistic traffic (e.g., email, file transfers, VoIP).
- **Routing Protocols Tested** :
- **RIP** : Chose paths based on hop count (number of routers).
- **EIGRP** : Used bandwidth, delay, and load for path selection.
- **Optimization** : Applied Quality of Service (QoS) to prioritize VoIP traffic.
- **Metrics Measured** : Latency (delay), packet loss, throughput (data rate).

### Outcomes

- **RIP** : Converged slowly (up to 180 seconds after a link failure), with 5% packet loss for VoIP.
- **EIGRP** : Converged in under 10 seconds, reducing packet loss to 1%.
- **QoS Impact** : VoIP latency dropped from 200 ms to 50 ms, improving call quality.
- **Real-World Impact** : The company switched to EIGRP, saving costs on downtime and improving productivity.

### Research Insights

- **Why It Matters** : EIGRP’s composite metric (bandwidth + delay) outperforms RIP’s simple hop count in dynamic networks.
- **For Scientists** : Simulate similar scenarios in NS-3 to compare EIGRP with OSPF or AI-based routing (e.g., RouteNet-Fermi, 2025). Explore how QoS affects fairness in traffic prioritization.

  _Source_ : Adapted from enterprise case studies on Scribd and Riverbed’s OPNET documentation.

---

## Case Study 2: MANET Routing in Disaster Response Networks

### Context

Mobile Ad Hoc Networks (MANETs) are used in disaster zones where traditional networks fail (e.g., after earthquakes). A 2024 study (DIVA-Portal) tested **AODV (Ad Hoc On-Demand Distance Vector)** and **OLSR (Optimized Link State Routing)** to connect rescue team devices.

### Technical Details

- **Network Setup** : 50 mobile nodes (e.g., smartphones, drones) in a 1 km² area.
- **Simulation Tool** : NS-2 (similar to NS-3), modeling node mobility and random traffic.
- **Protocols Tested** :
- **AODV** : Builds paths only when needed, saving energy.
- **OLSR** : Maintains a full network map, updating proactively.
- **Optimization** : Tuned AODV’s route request frequency to reduce overhead.
- **Metrics** : Packet Delivery Ratio (PDR), latency, energy consumption.

### Outcomes

- **AODV** : Higher PDR (95%) in sparse networks but higher latency (100 ms).
- **OLSR** : Better in dense networks (90% PDR, 50 ms latency).
- **Optimization** : Adjusting AODV’s route requests improved throughput by 15%.
- **Real-World Impact** : MANETs enabled reliable communication for rescue operations in a simulated disaster scenario.

### Research Insights

- **Why It Matters** : MANETs are critical for dynamic, infrastructure-less environments.
- **For Scientists** : Experiment with NS-3 to test hybrid protocols (e.g., combining AODV and OLSR). Use the UOS_IOTSH_2024 dataset to simulate IoT-based disaster networks.

  _Source_ : DIVA-Portal study on MANET routing, 2024.

---

## Case Study 3: Vehicular Ad Hoc Networks (VANETs) with OLSR

### Context

VANETs connect cars for applications like autonomous driving. A 2024 HighTech Journal study optimized **OLSR** for VANETs to ensure low-latency communication in high-mobility scenarios.

### Technical Details

- **Network Setup** : 100 vehicles on a highway, each with a Wi-Fi-like device.
- **Simulation Tool** : OMNeT++ with Veins framework, modeling vehicle movement.
- **Protocol** : OLSR, which proactively shares link-state information.
- **Optimization** : Adjusted OLSR’s topology update frequency to handle fast-moving cars.
- **Metrics** : Latency, packet loss, route stability.

### Outcomes

- **Before Optimization** : High mobility caused 20% packet loss, 150 ms latency.
- **After Optimization** : Packet loss dropped to 5%, latency to 30 ms.
- **Real-World Impact** : Enabled real-time collision avoidance messages for self-driving cars.

### Research Insights

- **Why It Matters** : Low latency is critical for safety in VANETs.
- **For Scientists** : Simulate VANETs in OMNeT++ with 5G parameters. Explore AI-driven routing (e.g., RouteNet-Fermi, 2025) to predict vehicle movement and optimize paths.

  _Source_ : HighTech Journal, 2024.

---

## Case Study 4: Energy-Efficient Routing in Wireless Sensor Networks (WSNs)

### Context

WSNs power IoT devices like environmental sensors, which need energy-efficient routing. A 2024 ScienceDirect study used a **fuzzy cuckoo search algorithm** to optimize routing in WSNs.

### Technical Details

- **Network Setup** : 200 sensor nodes in a 500x500 m area.
- **Simulation Tool** : MATLAB, modeling energy consumption and data transmission.
- **Protocol** : Modified LEACH (Low-Energy Adaptive Clustering Hierarchy).
- **Optimization** : Fuzzy logic prioritized nodes with high energy and short paths.
- **Metrics** : Network lifetime, energy consumption, delay.

### Outcomes

- **Standard LEACH** : Network lasted 1000 rounds, 200 ms delay.
- **Fuzzy Cuckoo Search** : Extended lifetime to 1500 rounds, reduced delay to 150 ms.
- **Real-World Impact** : Improved monitoring in smart agriculture (e.g., soil sensors).

### Research Insights

- **Why It Matters** : Energy efficiency is crucial for battery-powered IoT devices.
- **For Scientists** : Implement fuzzy logic in NS-3 for WSN simulations. Use the GenNP dataset (2024) to test energy-efficient protocols for IoT.

  _Source_ : ScienceDirect, 2024.

---

## Case Study 5: IP Network Optimization at Princeton

### Context

Princeton University optimized its campus IP network to handle high traffic (e.g., student streaming, research data). They used mathematical modeling to tune intradomain routing protocols.

### Technical Details

- **Network Setup** : 50 routers, 10 LANs across campus buildings.
- **Simulation Tool** : Custom Python scripts with NetworkX for traffic analysis.
- **Protocol** : OSPF with traffic engineering.
- **Optimization** : Adjusted link weights using linear programming to balance load.
- **Metrics** : Throughput, latency, congestion.

### Outcomes

- **Before** : Peak traffic caused 300 ms latency, 10% packet loss.
- **After** : Latency reduced to 50 ms, packet loss to 2%.
- **Real-World Impact** : Faster research data transfers and smoother online classes.

### Research Insights

- **Why It Matters** : Mathematical optimization ensures scalability in large networks.
- **For Scientists** : Use linear programming (e.g., PuLP in Python) to optimize link weights. Explore SDN (Software-Defined Networking) for dynamic load balancing, per 2025 studies.

  _Source_ : Adapted from Princeton networking research.

---

## Additional Research Notes

- **Recent Advances** : 2024 MDPI study on TOM-optimized QoS improved Packet Delivery Ratio by 10% in enterprise networks.
- **Datasets** : Use CAIDA ([https://www.caida.org](https://www.caida.org/)) or UOS_IOTSH_2024 for real-world traffic analysis.
- **Future Exploration** : Combine AI (RouteNet-Fermi, 2025) with quantum routing for next-gen networks.

These case studies show how routing, optimization, and simulation solve real problems, from corporate networks to IoT. Use them as inspiration for your own simulations and research projects!
