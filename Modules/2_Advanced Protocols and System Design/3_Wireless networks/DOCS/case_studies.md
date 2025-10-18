# Case Studies on Wireless Networks: Real-World Applications

This document presents six detailed case studies showcasing practical applications of wireless networks (IEEE 802.11 Wi-Fi, channel access models, 5G architecture). Each case study is designed for researchers and aspiring scientists, providing real-world context, data-driven insights, and prompts for further investigation. These align with the Jupyter Notebook tutorial and Python simulations, bridging theory to practice.

## Case Study 1: 5G in Telemedicine and Remote Surgery

**Context** : 5G’s ultra-low latency (1 ms) and high bandwidth (up to 20 Gbps) enable real-time telemedicine, such as remote surgery.
**Example** : In 2019, China performed a remote brain surgery using 5G, where a surgeon in Beijing controlled robotic arms in a patient 3,000 km away. The latency was 1–2 ms, critical for precision.
**Technical Details** :

- **Architecture** : 5G RAN with mmWave (28 GHz) for high data rate; network slicing prioritized surgical data.
- **Math** : Latency = propagation + processing + queueing. Propagation = 3000 km / 3e8 m/s ≈ 10 ms (reduced by edge computing to 1 ms).
- **Impact** : Success rate >95% in trials; enabled access to specialists in rural areas.
  **Research Prompt** : Model 5G slicing for telemedicine using NS-3. How does prioritizing traffic affect latency under interference?
  **Connection to Tutorial** : See 5G architecture (Section 5) and latency math (Section 5.3). Simulate with `mimo_throughput.py`.

## Case Study 2: Private 5G Networks in Smart Manufacturing

**Context** : Private 5G networks provide secure, reliable connectivity for industrial IoT, improving automation.
**Example** : Siemens deployed a private 5G network in a German factory (2021), connecting 100+ robots and AR devices for maintenance.
**Technical Details** :

- **Architecture** : Sub-6 GHz 5G with Massive MIMO (32x32 antennas) for coverage; OFDMA for device sharing.
- **Math** : Throughput = B _ log₂(1 + SNR) _ min(Nt, Nr). For B=100 MHz, SNR=20, Nt=32, Nr=4: log₂(21)≈4.39, min=4, rate≈1.76 Gbps.
- **Impact** : Reduced downtime by 30%; AR maintenance cut repair time by 40%.
  **Research Prompt** : Simulate factory interference in NS-3. Can hybrid OFDMA-TDMA improve robot coordination?
  **Connection to Tutorial** : See 5G sharing (Section 5.3) and `traffic_analysis.py` for similar data patterns.

## Case Study 3: Wi-Fi 6 vs. 5G in Indoor Enterprise Networks

**Context** : Wi-Fi 6 (802.11ax) competes with 5G for indoor high-density environments due to cost and unlicensed bands.
**Example** : A 2022 study in a London office (ScienceDirect) showed Wi-Fi 6 handled 200 devices better than 5G indoors, saving 40% on infrastructure.
**Technical Details** :

- **Architecture** : Wi-Fi 6 with OFDMA, 5 GHz, 80 MHz channels; CSMA/CA for access.
- **Math** : Rate = B _ log₂(M) _ N _ R. For B=80 MHz, 256-QAM (M=256, log₂=8), N=2, R=5/6: 80e6 _ 8 _ 2 _ 0.833 ≈ 1.07 Gbps.
- **Impact** : Wi-Fi 6 achieved 90% throughput efficiency vs. 70% for 5G indoors (due to mmWave blockage).
  **Research Prompt** : Use `csma_ca_collision.py` to model Wi-Fi 6 in dense setups. Can MU-MIMO reduce collisions further?
  **Connection to Tutorial** : See Wi-Fi standards (Section 3.1) and CSMA/CA (Section 4.2).

## Case Study 4: Wi-Fi Evolution in Urban Monitoring

**Context** : Wi-Fi networks in cities provide data for urban planning and security analysis.
**Example** : CRAWDAD dataset (2006–2010, Lawrence, KS) tracked Wi-Fi growth. In 2006, 70% of networks used WEP (weak); by 2010, 80% adopted WPA2.
**Technical Details** :

- **Architecture** : 802.11b/g (2.4 GHz), transitioning to 802.11n (MIMO).
- **Math** : Collision prob p ≈ 1/(CW+1). For CW=15, n=20 APs: p=1/16, effective p=1-(1-1/16)^20≈0.72, slowing networks.
- **Impact** : WPA3 adoption by 2020 reduced unsecured networks to <10%, improving urban IoT security.
  **Research Prompt** : Analyze Wi-Fi 6E (6 GHz) in NS-3 for urban density. Can channel expansion reduce p?
  **Connection to Tutorial** : See Wi-Fi security (Section 3.5) and `csma_ca_collision.py`.

## Case Study 5: 5G in Smart Ports

**Context** : 5G enhances logistics with real-time tracking and automation.
**Example** : Bari, Italy (2020, MDPI) used 5G for smart port logistics, connecting cranes, trucks, and sensors.
**Technical Details** :

- **Architecture** : 5G with network slicing for cargo tracking; V2X for vehicle communication.
- **Math** : Latency <1 ms via edge computing; coverage prob = exp(-λ π r²). For λ=0.0001/km², r=100 m: exp(-0.0001*π*10000)≈0.73 (73% coverage).
- **Impact** : Improved cargo processing by 50%; reduced delays by 20%.
  **Research Prompt** : Model slicing in Python. How does prioritization affect throughput under load?
  **Connection to Tutorial** : See 5G slicing (Section 5.2) and `mimo_throughput.py`.

## Case Study 6: 5G for Autonomous Vehicles

**Context** : 5G’s low latency and V2X enable vehicle communication for safety.
**Example** : A 2023 PMC study showed 5G V2V reduced collision rates by 90% in simulations for self-driving cars.
**Technical Details** :

- **Architecture** : mmWave 5G with TDD; HARQ for reliable data.
- **Math** : Latency = 1 μs (prop) + 0.5 ms (proc) + 0.4 ms (queue) ≈ 1 ms. Compare to 4G: 50 ms.
- **Impact** : Enabled real-time obstacle avoidance; scaled to 100 vehicles/km².
  **Research Prompt** : Simulate V2X in NS-3. Can beamforming improve mmWave reliability?
  **Connection to Tutorial** : See 5G features (Section 5.4) and latency math (Section 5.3).

  **Notebook Tip** : For each case, note the key wireless feature (e.g., slicing, OFDMA) and run related Python scripts (`traffic_analysis.py` for Case 2, 5; `csma_ca_collision.py` for Case 3, 4).
