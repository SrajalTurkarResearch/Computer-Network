# Transport Layer Case Studies

These case studies bring the transport layer to life, showing how TCP and UDP mechanics, flow control, and congestion control shape real-world networks. Each case provides context, technical details, lessons, and research ideas for your scientific journey. Think of them as experiments in a lab, revealing the transport layer’s impact.

## Case Study 1: 1986 ARPANET Congestion Collapse

**Context** : In 1986, the early internet (ARPANET) slowed dramatically, with throughput dropping from 32 Kbps to 40 bps—a 1000x reduction. Heavy traffic overwhelmed networks without proper controls.

**Technical Analysis** :

- **Problem** : No congestion control in early TCP. Senders flooded links, causing packet drops and retransmissions, spiraling into collapse.
- **Solution** : Van Jacobson introduced AIMD (Additive Increase Multiplicative Decrease) in 1988. Slow start and congestion avoidance halved the congestion window (cwnd) on loss, stabilizing networks. (Source: LBNL paper, Jacobson 1988)
- **Mechanics** : TCP retransmissions used sequence numbers (SEQ) and acknowledgments (ACK). Without cwnd limits, retransmits clogged routers.

  **Lessons** :

- Congestion control is critical to prevent network collapse.
- AIMD balances fairness and efficiency, like traffic lights managing cars.

  **Real-World Analogy** : A highway jam where everyone speeds up, crashes, and retries, worsening the clog. AIMD is like coordinated braking.

  **Research Implications** : Simulate 1986 collapse in ns-3 to test modern algorithms (e.g., BBR vs. AIMD). Explore AI-driven congestion prediction for 6G networks.

## Case Study 2: 2020 Zoom Surge

**Context** : During the 2020 pandemic, Zoom’s usage skyrocketed, straining internet infrastructure. TCP’s reliability ensured stable calls despite surges.

**Technical Analysis** :

- **Mechanics** : Zoom uses TCP for signaling (connection setup) and UDP for audio/video (low latency). TCP’s three-way handshake (SYN, SYN-ACK, ACK) ensured reliable session starts.
- **Flow Control** : Receivers advertised receiver window (rwnd) to pace data, preventing buffer overflow on low-end devices.
- **Congestion Control** : TCP Reno/CUBIC adjusted cwnd to avoid network overload. UDP relied on app-level throttling (e.g., reducing video quality).
- **Outcome** : Internet held up due to TCP’s dynamic adjustments, unlike 1986. (Source: IEEE Communications Magazine, 2020)

  **Lessons** :

- TCP’s flow and congestion control scale under pressure.
- UDP’s speed suits real-time apps but needs app-level controls.

  **Real-World Analogy** : Like a postal system delivering critical letters (TCP) and flyers (UDP) during a rush—letters arrive perfectly, flyers may not.

  **Research Implications** : Analyze Zoom traces (Wireshark) for cwnd/rwnd patterns. Test QUIC (UDP-based) for future video platforms.

## Case Study 3: Starlink TCP Performance (2025)

**Context** : Starlink’s low-earth orbit (LEO) satellites provide high-speed internet but face variable latency (20-50ms). TCP’s performance is critical.

**Technical Analysis** :

- **Challenge** : LEO satellites have dynamic RTTs due to handoffs. Traditional TCP (CUBIC) struggles with rapid changes.
- **Solution** : Google’s BBR (Bottleneck Bandwidth and RTT) outperforms CUBIC by estimating bandwidth-delay product (BDP = BW \* RTT) and pacing sends. BBRv3 (2023) and BBR.Swift (2024) further optimize for low-latency. (Source: ACM SIGCOMM 2025)
- **Mechanics** : TCP handshake adapts to variable RTTs; SACK (Selective ACK) reduces retransmits for bursty losses.
- **Outcome** : BBR achieves 10-20% higher throughput than CUBIC in Starlink tests.

  **Lessons** :

- Modern congestion control (BBR) excels in dynamic networks.
- TCP’s reliability ensures data integrity over satellites.

  **Real-World Analogy** : Like adjusting a telescope’s focus for moving stars—BBR tracks network changes dynamically.

  **Research Implications** : Simulate Starlink in Mininet with BBR. Propose BBR extensions for interplanetary networks (high RTT).

## Case Study 4: 5G mmWave and MSS-TCP (2025)

**Context** : 5G mmWave offers ultra-high speeds (1-10 Gbps) but rapid signal fluctuations in urban areas (e.g., blockages by buildings).

**Technical Analysis** :

- **Challenge** : mmWave’s bandwidth swings (100 Mbps to 1 Gbps) confuse standard TCP, causing underuse or congestion.
- **Solution** : MSS-TCP (Multi-Scale Sliding TCP, 2024) adapts cwnd and rwnd dynamically using machine learning to predict signal changes. (Source: System Communications and Networks, 2024)
- **Mechanics** : Flow control adjusts rwnd for device buffers; congestion control uses RL-based cwnd tuning, reducing latency by 20-30%.
- **Outcome** : MSS-TCP boosts throughput in 5G urban deployments (e.g., smart cities).

  **Lessons** :

- Advanced TCP variants leverage AI for next-gen networks.
- Flow and congestion control must sync for high-speed links.

  **Real-World Analogy** : Like a self-driving car adjusting speed for sudden obstacles—MSS-TCP predicts network shifts.

  **Research Implications** : Test MSS-TCP in 5G testbeds (e.g., ORAN). Develop RL models for 6G transport layer optimization.
