# Quantum Networking Cheat Sheet

 **Purpose** : Quick reference for quantum networking concepts from the tutorial (October 18, 2025). Use alongside Python projects (`secure_banking_qkd.py`, etc.) to master quantum science. Keep this in your notebook for rapid recall.

## 1. Core Concepts

* **Quantum Networking** : Uses qubits (quantum bits) and entanglement for secure, fast communication.
* *Why* : Unhackable security (QKD), distributed quantum computing.
* *Real-World* : Chicago’s 2025 network, DARPA QuANET (6.8 Mbps).
* **Classical Networks** : Bits (0 or 1), OSI layers, TCP/IP. Vulnerable to quantum attacks (RSA).
* *Equation* : Shannon capacity $B = W \log_2(1 + \frac{S}{N})$ (e.g., 2 Mbps for $W=1$ MHz, $S/N=3$).

## 2. Quantum Mechanics Basics

* **Wave-Particle Duality** : Particles act as waves or dots. Wavelength $\lambda = \frac{h}{p}$, $h = 6.626 \times 10^{-34}$ J·s.
* *Example* : Electron $\lambda \approx 0.7$ nm ($m=9 \times 10^{-31}$ kg, $v=10^6$ m/s).
* **Uncertainty Principle** : $\Delta x \cdot \Delta p \geq \frac{h}{4\pi}$. Prevents qubit cloning.
* **Measurement** : Collapses state, e.g., $|\psi\rangle = 0.6|0\rangle + 0.8|1\rangle$, $P(0) = 0.36$, $P(1) = 0.64$.
* **Hilbert Space** : Qubit state $|\psi\rangle = a|0\rangle + b|1\rangle$, $|a|^2 + |b|^2 = 1$.

## 3. Qubits

* **Superposition** : Qubit = $\alpha|0\rangle + \beta|1\rangle$, e.g., $\alpha = \beta = \frac{1}{\sqrt{2}}$ (50% each).
* *Code* : `qc.h(0)` in `superposition_simulation.py`.
* **Gates** : Hadamard $H = \frac{1}{\sqrt{2}} \begin{bmatrix} 1 & 1 \ 1 & -1 \end{bmatrix}$, creates superposition.
* **Multi-Qubits** : 2 qubits = 4 states ($|00\rangle$, $|01\rangle$, $|10\rangle$, $|11\rangle$).

## 4. Entanglement

* **Definition** : Linked particles, e.g., $|\Phi^+\rangle = \frac{1}{\sqrt{2}}(|00\rangle + |11\rangle)$.
* *Code* : `qc.h(0); qc.cx(0,1)` in `entanglement_simulation.py`.
* **Use** : QKD, teleportation, distributed computing (Aliro’s 50+ devices).
* **Bell Test** : Quantum correlation > 2 (classical max), up to $2\sqrt{2} \approx 2.8$.

## 5. Quantum Key Distribution (QKD)

* **BB84 Protocol** : Alice sends qubits in random bases (+/x), Bob measures. Error rate $Q$, key rate $R = 1 - 2h(Q)$, $h(Q) = -Q \log_2 Q - (1-Q) \log_2 (1-Q)$.
* *Example* : $Q=0.1$, $R \approx 0.07$.
* *Code* : `simulate_bb84` in `bb84_simulation.py`, `secure_banking_qkd.py`.
* **E91** : Entanglement-based, checks Bell violations.
* **Real-World** : China’s Micius, Chicago’s 2025 banking network.

## 6. Quantum Repeaters

* **Purpose** : Extend entanglement over distance (loss $e^{-d/L}$, $L \approx 22$ km).
* **Swapping** : Link A-Repeater-B to A-B. Success $\eta^2$ (e.g., $\eta=0.5$, success = 0.25).
* **Purification** : Boost fidelity, e.g., $F=0.8$ to $F' \approx 0.98$.
* *Equation* : $F' = \frac{F^2 + \frac{(1-F)^2}{3}}{F^2 + 2 \frac{(1-F)^2}{3}}$.

## 7. Quantum Communication Primitives

* **Teleportation** : Move qubit state with entanglement, 2 classical bits.
* *Code* : `teleportation_simulation.py`, fidelity $1 - 1.5p$ ($p=0.05 \rightarrow 0.925$).
* **Superdense Coding** : 2 bits via 1 qubit with entanglement.

## 8. Network Architectures

* **Layers** : Physical (photons), link (entanglement), network (routing).
* **Hardware** : Photon sources (ytterbium-171), detectors (superconducting).
* **Software** : QnodeOS (Inria 2025).

## 9. Challenges

* **Decoherence** : Environment disrupts qubits ($1-p$ survival, $p=0.01$).
* **Error Correction** : Shor code (9 qubits protect 1).
* **Hybrid Integration** : Classical-quantum synergy (DARPA QuANET).

## 10. Advanced Topics

* **Quantum Routing** : Optimize path fidelity $\prod F_i$ (e.g., 3 segments $F_i=0.9$, total = 0.729).
* *Code* : `distributed_qc_network.py`.
* **Post-Quantum Crypto** : Lattice-based, resists quantum attacks (NIST 2025).

## 11. Real-World Applications

* **Banking** : Secure transfers (Chicago 2025, `secure_banking_qkd.py`).
* **Distributed QC** : Networked qubits (Cisco, IonQ, `distributed_qc_network.py`).
* **Hybrid Networks** : 6.8 Mbps (DARPA, `hybrid_network_sim.py`).
* **Entanglement Networks** : 50+ devices (Aliro, `entanglement_distribution.py`).

## 12. Quick Code Snippets

* **Superposition** : `from qiskit import QuantumCircuit; qc = QuantumCircuit(1,1); qc.h(0);`.
* **Entanglement** : `qc.h(0); qc.cx(0,1);`.
* **BB84** : `def simulate_bb84(n_bits): ...` (see `bb84_simulation.py`).
* **Network Graph** : `import networkx as nx; G = nx.path_graph(50);` (see `entanglement_distribution.py`).

## 13. Research Tips

* Run projects, tweak parameters (e.g., distance in `secure_banking_qkd.py`).
* Sketch: Bloch sphere, repeater chain, network graphs.
* Read: 2025 Nature on multiplexing, Fermilab reports.
* Reflect: Design a global QKD protocol or satellite repeater.

 **Keep This Handy** : Use with tutorial and projects to master quantum networking. You’re on the path to innovate like Einstein and Tesla!
