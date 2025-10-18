# Glossary of Key Terms – Decoding the Language of the Transport Layer

As a confluence of Turing's logic, Einstein's relativity, and Tesla's ingenuity, this glossary deciphers the transport layer's lexicon. Updated September 2025, it includes all terms from the tutorial, with definitions, logic, analogies, examples, math ties, and research pointers. Use as a reference for your notes – each entry builds understanding for scientific pursuits.

## Alphabetical Glossary

- **ACK (Acknowledgment):** Control confirming receipt; number = next expected SEQ. Logic: Enables cumulative feedback. Analogy: Receipt for mail. Example: Browser ACKs web chunks. Math: ACK = SEQ + len +1 (SYN/FIN). Research: Delayed ACKs in QUIC (2025 optimizations).
- **AIMD (Additive Increase Multiplicative Decrease):** CC algorithm: Linear increase (+1/RTT), halve on loss. Logic: Probes capacity fairly. Analogy: Gradual acceleration, hard brake. Example: Stabilized 1986 internet. Math: Equilibrium cwnd ≈ sqrt(1.5/p) × MSS/RTT. Research: RL extensions (arXiv Aug 2025).
- **BDP (Bandwidth-Delay Product):** In-flight data: BW × RTT. Logic: Sets optimal window. Analogy: Pipeline capacity. Example: 10Gbps × 100ms = 125MB. Math: BDP = BW (bits/s) × RTT /8 (bytes). Research: BBR estimation in Starlink (ACM Jul 2025).
- **Checksum:** 16-bit error detector (one's complement sum). Logic: Validates integrity. Analogy: Fingerprint. Example: Bit flip in Wi-Fi drops packet. Math: ~sum(16-bit words + carry). Research: Partial in UDP-Lite.
- **Cwnd (Congestion Window):** Sender limit on unACKed data. Logic: Controls network load. Analogy: Traffic valve. Example: Shrinks in Wi-Fi jams. Math: Growth: ×2/RTT (slow start). Research: RL tuning (2025).
- **Datagram:** UDP's self-contained unit. Logic: Independent delivery. Analogy: Postcard. Example: DNS response. Math: Max 65KB. Research: Options draft (IETF 2025).
- **Dup ACK (Duplicate Acknowledgment):** Repeated ACK signals loss. Logic: Triggers fast retransmit. Analogy: Crowd repeating request. Example: Mobile handoff drops. Math: 3 threshold. Research: In SACK.
- **ECN (Explicit Congestion Notification):** Router marks for early warning. Logic: Reduces loss. Analogy: Yellow light. Example: Datacenters. Math: CE bit in IP/TCP. Research: QUIC integration.
- **FIN (Finish):** Closes data stream. Logic: Graceful shutdown. Analogy: Phone hang-up. Example: Web socket close. Math: Consumes 1 SEQ. Research: Half-close in streaming.
- **FlightSize:** UnACKed bytes in transit. Logic: Caps sends. Analogy: Planes airborne. Example: Bursty video. Math: Sent - ACKed. Research: BBR drain phase.
- **IRS (Initial Receive Sequence Number):** Server's starting SEQ. Logic: Syncs with client. Analogy: Book starting page. Example: Anti-replay. Math: Random 32-bit. Research: Crypto IRS.
- **ISS (Initial Send Sequence Number):** Client's starting SEQ. Logic: Avoids old packet confusion. Analogy: Raffle ticket start. Example: API calls. Math: Clock + random. Research: Entropy in IoT.
- **MSS (Maximum Segment Size):** Max TCP data per segment. Logic: Fits MTU. Analogy: Box size. Example: 1460 Ethernet. Math: MTU -40. Research: PMTUD in IPv6.
- **MTU (Maximum Transmission Unit):** Link's max packet. Logic: Avoids fragmentation. Analogy: Door width. Example: VPN reduces. Math: Path MTU = min(links). Research: Black holes.
- **Nagle's Algorithm:** Coalesces small sends. Logic: Reduces overhead. Analogy: Fill car before drive. Example: Telnet. Math: Timer 200ms. Research: Latency in robotics.
- **Port:** 16-bit app identifier. Logic: Multiplexing. Analogy: Apartment number. Example: 443 HTTPS. Math: 65K total. Research: NAT exhaustion.
- **PUSH Flag:** Delivers data immediately. Logic: Bypasses buffering. Analogy: Express mail. Example: SSH prompts. Math: Semantic. Research: AR/VR low-latency.
- **RTT (Round-Trip Time):** Packet + ACK time. Logic: Timeout base. Analogy: Echo delay. Example: Satellite 500ms. Math: SRTT = 0.875×old + 0.125×new. Research: ML forecasting.
- **RTO (Retransmission Timeout):** Resend wait time. Logic: Adapts to variance. Analogy: Repeat question timer. Example: Flaky Wi-Fi. Math: SRTT +4×RTTvar. Research: DTN space.
- **Rwnd (Receiver Window):** Advertised buffer space. Logic: Flow pacing. Analogy: Party guest limit. Example: IoT small rwnd. Math: Throughput = rwnd/RTT. Research: Cloud auto-scale.
- **SACK (Selective Acknowledgment):** ACKs non-contiguous blocks. Logic: Efficient recovery. Analogy: Specify missing pages. Example: Wireless bursts. Math: 4 ranges/option. Research: With FEC.
- **Segment:** TCP's data unit. Logic: Ordered chunks. Analogy: Book chapters. Example: Email parts. Math: Ceil(data/MSS). Research: Jumbo in GigE.
- **SEQ (Sequence Number):** Byte position tracker. Logic: Ordering/dupe detection. Analogy: Page numbers. Example: Video reassembly. Math: 32-bit wrap. Research: 64-bit high-speed.
- **Ssthresh (Slow Start Threshold):** Exponential to linear switch. Logic: Growth phase change. Analogy: Speed limit. Example: Initial 64KB. Math: FlightSize/2 on loss. Research: Dynamic in Vegas.
- **SYN (Synchronize):** Handshake start. Logic: SEQ sync. Analogy: Conversation opener. Example: SYN flood DoS. Math: +1 to ACK. Research: Cookies defense.
- **SYN-ACK:** Server handshake reply. Logic: Mutual sync. Analogy: "Got you, my turn." Example: Unreachable timeout. Math: ACK=ISS+1. Research: TFO skip.
- **TIME-WAIT:** Post-close absorption state. Logic: Straggler handling. Analogy: Party linger. Example: Server port reuse. Math: 2×MSL=240s. Research: Kernel scaling.
- **URG (Urgent):** Out-of-band data flag. Logic: Priority interrupt. Analogy: Emergency alert. Example: Telnet escapes. Math: Pointer to urgent byte. Research: WebSocket alternatives.

**2025 Additions:**

- **MSS-TCP:** Multi-scale CC for mmWave (cwnd via ML).
- **RL-TCP:** Reinforcement learning for adaptive CC.
- **UDP Options:** IETF extension for UDP features.

This glossary is your decoding key – reference during simulations. Forge ahead, researcher!
