# Cheat Sheet: Performance Modeling with Markov Chains in Computer Networks

**Overview** : Quick reference for beginners to researchers. Covers fundamentals, math, code, visuals, applications, and research. Inspired by Turing (computation), Einstein (probabilistics), Tesla (networks). Use for notes, exams, or projects. Key: ρ = λ/μ (utilization); assume ρ < 1 for stability.

## 1. Fundamentals of Networks & Metrics

- **Networks** : Nodes (devices), Links (wired/wireless), Routers (directors), Protocols (TCP/IP).
- **Types** : LAN (local), WAN (internet), MAN (city), PAN (Bluetooth).
- **Packets** : Header (address) + Payload (data); random arrivals (Poisson λ).
- **Metrics** :
- Latency: Propagation + Transmission + Queuing + Processing.
- Throughput: Data rate (bps); ≈ μ(1 - π_0).
- Loss: π_K (full buffer).
- Jitter: Delay variance.
- **Analogy** : Network = city roads; packets = cars; queues = traffic jams.

## 2. Markov Chains Basics

- **Definition** : Stochastic process; next state depends only on current (memoryless).
- **Components** : States (e.g., Idle/Busy); Transition Matrix P (rows sum to 1); Steady-State π = πP, ∑π=1.
- **Types** : DTMC (discrete steps), CTMC (continuous, Q matrix: πQ=0).
- **Poisson Process** : Arrivals rate λ; exponential times.
- **Formula** : π(k+1) = π(k) × P; long-run π solves linear system.
- **Code Snippet** (Steady-State):
  ```python
  import numpy as np
  P = np.array([[0.8, 0.2], [0.3, 0.7]])  # Idle/Busy
  A = np.transpose(P - np.eye(2)); A = np.vstack((A, [1,1])); b = np.array([0,0,1])
  pi = np.linalg.lstsq(A, b, rcond=None)[0]  # Output: [0.6, 0.4]
  ```
- **Visual** : State diagram (circles + arrows with probs).

## 3. Queueing Models

- **M/M/1** : Single server; arrivals λ, service μ.
- ρ = λ/μ <1.
- Queue Length L = ρ/(1-ρ).
- Queuing Delay W_q = L/λ = 1/(μ-λ).
- System Time W = W_q + 1/μ.
- **M/M/1/K** : Finite buffer K; π_k = (1-ρ)ρ^k / (1-ρ^{K+1}); Loss = π_K.
- **M/M/c** : c servers; Throughput = cμ(1-π_0).
- **Advanced** : Stiff chains (uniformization for rare events); MMPP (modulated rates).
- **Code Snippet** (M/M/1 Simulation):
  ```python
  import random
  lambda_rate, mu_rate, sim_time = 10, 15, 1000
  queue, time, total_wait, packets = 0, 0, 0, 0
  while time < sim_time:
      arrival = random.expovariate(lambda_rate)
      service = random.expovariate(mu_rate) if queue > 0 else float('inf')
      if arrival < service:
          queue += 1; packets += 1; time += arrival
      else:
          queue -= 1; total_wait += queue / lambda_rate; time += service
  avg_delay = (total_wait / packets) * 1000  # ms
  ```
- **Visual** : Plot W_q vs. ρ (exponential rise).

## 4. Latency & Throughput Analysis

- **Latency** : Total delay; queuing dominates (W_q = 1/(μ-λ)).
- **Throughput** : μ(1-π_0) for M/M/1; λ(1-π_K) for M/M/1/K.
- **Example** : λ=10, μ=15 → ρ=0.667, W_q=200ms, Throughput=10 packets/sec.
- **Code Snippet** (Plot Latency):
  ```python
  import numpy as np; import matplotlib.pyplot as plt
  rho = np.linspace(0.01, 0.99, 100); mu=15
  W_q = 1 / (mu * (1 - rho)) - 1 / mu
  plt.plot(rho, W_q * 1000); plt.xlabel('ρ'); plt.ylabel('Delay (ms)'); plt.show()
  ```

## 5. Applications & Real-World

- **CDNs (e.g., Akamai)** : Model spikes; reduce latency <5s.
- **5G/6G** : Handoffs (states: Connected/Handing Off).
- **IoT/Cloud** : Throughput in AWS; predict overloads.
- **Visual** : Histogram of arrivals (Poisson).

## 6. Research Directions & Insights

- **Hybrids** : Markov + AI for non-stationary traffic.
- **Quantum/6G** : Model entanglement delays.
- **Rare** : Stiff chains (uniformization); symbolic solutions (SymPy).
- **Projects** : Mini: Add K to simulation. Major: Analyze CIC-IDS2017 (download: unb.ca/cic/datasets).
- **Exercises** : 1. Solve π for P=[[0.7,0.3],[0.4,0.6]] → [0.571,0.429]. 2. Simulate M/M/1/K=5.

## 7. Tools & Next Steps

- **Python Libs** : NumPy (math), Matplotlib (plots), NetworkX (graphs).
- **Sim Tools** : ns-3 for networks.
- **Read** : "Queueing Networks and Markov Chains" (Bolch et al.).
- **Publish** : IEEE Transactions; e.g., "Markov for 6G Edge Computing".
- **Tip** : Validate with data; question assumptions like memoryless.

Print this sheet; laminate for lab use. As Tesla said, "The present is theirs; the future, for which I really worked, is mine."—apply Markov to shape network futures!
