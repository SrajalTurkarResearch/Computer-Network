# QoS in Computer Networks Cheatsheet: Quick Reference for Aspiring Scientists

As your guide in network science, channeling Turing's logic, Einstein's insights, and Tesla's innovation, this cheatsheet summarizes the QoS tutorial. Use it as a quick reference for formulas, concepts, algorithms, and tips. Print it, annotate it, and keep it handy for exams, simulations, or research. All content is from the tutorial—your sole resource for mastering QoS, queuing theory, and scheduling (WFQ, RED).

## 1. QoS Fundamentals

- **Definition:** Techniques to manage packet flow for reliable performance (prioritize, schedule, avoid congestion).
- **Goals (QoS Quartet):**
  - Low Latency: <100 ms for real-time.
  - High Throughput: Max data rate.
  - Low Jitter: Consistent delays (<20 ms).
  - Low Loss: <1% packets dropped.
- **Analogy:** Traffic cop on a highway (packets = cars, routers = intersections).
- **Key Challenge:** Congestion when λ (arrivals) > μ (service).

## 2. Queuing Theory Basics

- **Parameters:**
  - λ: Arrival rate (pkt/s).
  - μ: Service rate (pkt/s).
  - ρ: Utilization = λ / μ (<1 for stability).
  - Buffer Size: Finite (K) or infinite.
- **M/M/1 Model (Random arrivals/service, 1 server):**
  - L_q (Avg Queue Length) = ρ² / (1 - ρ).
  - W_q (Avg Wait Time) = L_q / λ (Little’s Law).
  - L (Avg System Length) = ρ / (1 - ρ).
  - W (Avg System Time) = W_q + 1/μ.
  - Poisson Arrival Prob: P(n) = (λt)^n \* e^{-λt} / n!.
- **Example:** ρ=0.8 → L_q=3.2, W_q=3.2/λ.
- **Advanced Models:**
  - M/M/c: Multiple servers; L_q complex (use SymPy).
  - M/M/1/K: Finite buffer; Drop Prob π_K = (1-ρ) ρ^K / (1-ρ^{K+1}).
  - M/D/1: Fixed service; L_q = ρ² / (2(1-ρ)).
- **Networks:** Jackson’s Theorem: Total delay = sum(W_i) for independent queues.
- **Tip:** As ρ → 1, queues explode—use QoS to stabilize.

## 3. Scheduling Algorithms

- **Classification:** DSCP tags (0-63): EF (urgent, 46), AF (assured), BE (default, 0).
- **FIFO:** First in, first out—simple, no priority.
- **WFQ (Weighted Fair Queuing):**
  - Share = φ_i / Σφ (φ = weight).
  - Finish Time F = max(prev F, arrival) + size / (rate \* share).
  - Fairness: Max-min (guarantees min bandwidth).
  - Example: φ_video=3, φ_data=1 → Video gets 75%.
- **PQ (Priority Queuing):** Strict levels; risk starvation.
- **CBWFQ:** WFQ per class (e.g., video class).
- **DRR (Deficit Round-Robin):** Cyclic, adjusts for size; O(1) complexity.
- **Comparison Table:**

| Algorithm | Fairness | Complexity | Best For      |
| --------- | -------- | ---------- | ------------- |
| FIFO      | None     | Low        | Simple        |
| WFQ       | Weighted | Medium     | Multimedia    |
| PQ        | Strict   | Low        | Real-time     |
| DRR       | Fair     | Low        | Variable pkts |

## 4. Congestion Avoidance

- **Tail-Drop Issue:** Global synchronization (yo-yo traffic).
- **RED (Random Early Detection):**
  - Q_avg = (1-w) Q_avg + w Q_instant (w=0.002).
  - P_drop = max_P \* (Q_avg - min_th) / (max_th - min_th) if min_th < Q_avg < max_th.
  - Example: min_th=5, max_th=15, max_P=0.1, Q_avg=10 → P_drop=0.05.
- **Variants:**
  - WRED: P_drop by DSCP (EF low, BE high).
  - ARED: Auto-tune max_P.
  - ECN: Mark packets instead of dropping.
- **Tip:** RED stabilizes TCP; simulate for bursty traffic.

## 5. Applications & Research Quick Tips

- **Apps:** 5G (PQ for URLLC), IoT (RED for sensors), Cloud (CBWFQ for ML), CERN (WFQ for data grids).
- **Research Directions:** AI-tuned RED, quantum queuing, 6G low-latency, green QoS.
- **Rare Insight:** Handle self-similar traffic (not Poisson) with fractal models.
- **Tools:** NS-3/OMNeT++ for sims; Python (SimPy) for queues.

## 6. Key Simulations & Code Snippets

- **M/M/1 Sim:** Use expovariate for arrivals/service; plot queue vs. time.
- **WFQ Sim:** Calc finish times; prioritize high φ.
- **RED Sim:** Update Q_avg, probabilistic drops.
- **Experiment Tip:** Vary ρ=0.5-0.95; compare sim avg L_q to theory.

## 7. Exercises & Projects Quick Ref

- **Exercise:** Calc L_q for ρ=0.7 → 1.63.
- **Mini Project:** Plot L_q vs. ρ (hockey stick curve).
- **Major Project:** Simulate WFQ+RED on synthetic traffic; measure delay.
- **Next Steps:** Read Kleinrock's "Queueing Systems"; attend IEEE INFOCOM.

This cheatsheet is your QoS compass—review formulas daily, simulate often. Questions? Probe deeper; science thrives on curiosity!
