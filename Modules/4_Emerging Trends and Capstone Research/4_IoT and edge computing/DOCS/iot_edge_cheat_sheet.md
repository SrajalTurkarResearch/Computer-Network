# Cheat Sheet: IoT and Edge Computing - Scalability and Latency Models

This cheat sheet summarizes the _IoT and Edge Computing: Scalability and Latency Models in Computer Networks_ tutorial for quick reference. Perfect for your scientific notes, it covers definitions, formulas, protocols, and research tips in simple terms.

## 1. Key Definitions

- **IoT (Internet of Things)**: Connecting everyday objects (e.g., sensors, lights) to the internet to share data.
  - _Example_: Smart thermostat adjusts room temperature via app.
- **Edge Computing**: Processing data near the device (e.g., on a car) instead of far-away cloud servers.
  - _Example_: Security camera detects motion locally.
- **Scalability**: Ability to handle more devices/data without slowing down.
  - _Types_: Vertical (bigger server), Horizontal (more servers).
- **Latency**: Time delay for data to travel and be processed.
  - _Components_: Propagation, Transmission, Queuing, Processing.

## 2. IoT Architecture Layers

1. **Perception**: Sensors (e.g., temperature) and actuators (e.g., motors).
2. **Network**: Sends data via Wi-Fi, 5G, Zigbee.
3. **Middleware**: Organizes data from different devices.
4. **Application**: Shows results (e.g., phone app).
5. **Business**: Handles money, ethics, privacy.

## 3. Key Protocols

- **MQTT**: Lightweight, publish/subscribe for IoT (e.g., sensors sending data).
- **CoAP**: For low-power devices (e.g., battery sensors).
- **Zigbee**: Mesh network for smart homes (e.g., Philips Hue lights).
- **5G/NB-IoT**: Fast/low-power for wide areas (e.g., smart cities).
- **6LoWPAN**: IPv6 for low-power devices.

## 4. Scalability Models

- **Formula**: Device growth: \( D(t) = D_0 \times 2^t \)
  - _Example_: \( D_0 = 100 \), \( t = 3 \): \( D(3) = 100 \times 8 = 800 \) devices.
- **Amdahl’s Law**: Limits speedup with more processors.
  - \( S = \frac{1}{(1-p) + \frac{p}{n}} \), where \( p \) = parallel portion, \( n \) = processors.
  - _Example_: \( p = 0.9 \), \( n = 4 \): \( S = 1 / (0.1 + 0.9/4) \approx 3.077 \).
- **Network Load**: \( Load = Devices \times Data Rate \).
  - _Example_: 1,000 devices, 500 bits/s: \( Load = 1,000 \times 500 / 10^6 = 0.5 \) Mbps.

## 5. Latency Models

- **Total Latency**: \( L = D*p + D_t + D_q + D*{proc} \)
  - \( D_p = \frac{\text{Distance}}{\text{Speed}} \) (speed ~200 km/ms in fiber).
  - \( D_t = \frac{\text{Packet Size}}{\text{Bandwidth}} \times 1000 \).
  - \( D_q \): Queuing delay (use M/M/1 model).
  - \( D\_{proc} \): Processing delay.
- **Example**:
  - Distance = 100 km, Packet = 10 KB (80,000 bits), Bandwidth = 100 Mbps, \( D*q = 0.2 \) ms, \( D*{proc} = 0.1 \) ms.
  - \( D_p = 100 / 200 = 0.5 \) ms.
  - \( D_t = 80,000 / 100,000,000 \times 1000 = 0.8 \) ms.
  - \( L = 0.5 + 0.8 + 0.2 + 0.1 = 1.6 \) ms.
- **M/M/1 Queue**: \( D_q = \frac{\rho}{1-\rho} \cdot \frac{1}{\mu} \), \( \rho = \frac{\lambda}{\mu} \).
  - _Example_: \( \lambda = 5/s \), \( \mu = 10/s \): \( \rho = 0.5 \), \( D_q = 0.5 / (1-0.5) / 10 = 0.1 \) s.

## 6. Network Topologies

- **Star**: Devices connect to one hub (simple, less scalable).
  - Links: \( n-1 \), where \( n \) = nodes.
- **Mesh**: Devices connect to each other (robust, complex).
  - Links: \( \frac{n(n-1)}{2} \). _Example_: \( n=5 \), Links = \( 5 \times 4 / 2 = 10 \).
- **Hybrid**: Combines for flexibility.

## 7. Real-World Use Cases

- **Smart Agriculture**: IoT sensors monitor soil, edge nodes control irrigation.
  - _Scalability_: Handles 10,000+ sensors.
  - _Latency_: Edge ~0.55 ms vs. Cloud ~5.55 ms.
- **Autonomous Vehicles**: Edge processes sensor data for braking (<10 ms).
  - _Scalability_: Supports fleets of millions.
  - _Latency_: Edge ~0.85 ms vs. Cloud ~3.35 ms.
- **Smart Cities**: IoT cameras and edge nodes manage traffic with 5G.
  - _Scalability_: 10,000 cameras city-wide.
  - _Latency_: Edge ~0.06 ms vs. Cloud ~1.06 ms.

## 8. Research Tips

- **Tools**: NS-3, OMNeT++, Cooja for network simulations.
- **Simulations**: Model scalability with NetworkX (Python).
- **AI Integration**: Use MobileNet for edge AI inference.
- **Future Trends**:
  - 6G: <1 ms latency by 2030.
  - Quantum Edge: Ultra-secure networks.
  - Green IoT: Energy harvesting (e.g., solar sensors).
- **Security**: Explore blockchain for secure scaling.
- **Papers**: Read IEEE Network, Communications for latest trends.

## 9. Common Challenges

- **Interoperability**: Use 6LoWPAN for standardization.
- **Energy**: NB-IoT for low power.
- **Security**: Lightweight cryptography for edge.

## 10. Quick Formulas

- **Device Density**: \( \rho = \frac{N}{A} \) (N = devices, A = area).
- **Effective Latency**: \( L*{eff} = f*{edge} \times L*{edge} + (1-f*{edge}) \times L\_{cloud} \).
- **Power**: \( P = \frac{V^2}{R} + \text{dynamic power} \).

## 11. Next Steps

- Run Python projects from the tutorial (e.g., `smart_agriculture_project.py`).
- Simulate larger networks (10,000+ devices) in NS-3.
- Study 6G protocols or quantum cryptography.
- Build a research project: Optimize edge placement with AI.

This cheat sheet is your quick guide to mastering IoT and edge computing. Keep it handy for revision and inspiration as you become a scientist like Turing or Tesla!
