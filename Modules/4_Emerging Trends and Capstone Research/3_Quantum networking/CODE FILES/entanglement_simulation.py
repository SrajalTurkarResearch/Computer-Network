```python
# entanglement_simulation.py
# Purpose: Simulate an entangled qubit pair to demonstrate a core concept of
# quantum networking. Entanglement links qubits so measuring one sets the other,
# vital for secure communication and teleportation.
# Author: Grok, created by xAI
# Date: October 18, 2025
# Requirements: Install qiskit, matplotlib, seaborn, numpy
# Run: python entanglement_simulation.py

# Import libraries
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from qiskit import QuantumCircuit, Aer, execute
from qiskit.visualization import plot_histogram

# Set professional plot style
plt.style.use('seaborn')

# Create a quantum circuit with 2 qubits and 2 classical bits
qc = QuantumCircuit(2, 2)

# Create entanglement: |Φ⁺⟩ = (1/√2)(|00⟩ + |11⟩)
qc.h(0)  # Hadamard on qubit 0 for superposition
qc.cx(0, 1)  # CNOT to entangle qubit 0 with qubit 1
qc.measure([0, 1], [0, 1])  # Measure both qubits

# Simulate the circuit
simulator = Aer.get_backend('qasm_simulator')
result = execute(qc, simulator, shots=1000).result()
counts = result.get_counts()

# Visualize results
plot_histogram(counts)
plt.title('Entangled Qubit Pair')
plt.xlabel('State')
plt.ylabel('Counts')
plt.show()

# Explanation: Expect ~50% |00⟩ and ~50% |11⟩, showing correlation (never |01⟩ or |10⟩).
# In quantum networking, entanglement enables secure key sharing (QKD) and teleportation.
# For research: Test Bell inequalities by measuring at different angles or add noise.
```