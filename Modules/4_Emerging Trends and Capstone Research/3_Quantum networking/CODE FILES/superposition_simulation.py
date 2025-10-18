```python
# superposition_simulation.py
# Purpose: Simulate a qubit in superposition using a Hadamard gate to demonstrate
# quantum networking fundamentals. A qubit in superposition is both 0 and 1 until
# measured, key for quantum communication protocols like QKD.
# Author: Grok, created by xAI
# Date: October 18, 2025
# Requirements: Install qiskit, matplotlib, seaborn, numpy
# Run: python superposition_simulation.py

# Import libraries
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from qiskit import QuantumCircuit, Aer, execute
from qiskit.visualization import plot_histogram

# Set professional plot style
plt.style.use('seaborn')

# Create a quantum circuit with 1 qubit and 1 classical bit
qc = QuantumCircuit(1, 1)

# Apply Hadamard gate to put qubit in superposition: |ψ⟩ = (1/√2)(|0⟩ + |1⟩)
qc.h(0)

# Measure the qubit to collapse it to |0⟩ or |1⟩
qc.measure(0, 0)

# Simulate the circuit
simulator = Aer.get_backend('qasm_simulator')  # Use Qiskit’s simulator
result = execute(qc, simulator, shots=1000).result()  # Run 1000 times
counts = result.get_counts()  # Get measurement outcomes

# Visualize results
plot_histogram(counts)
plt.title('Qubit in Superposition (Hadamard Gate)')
plt.xlabel('State')
plt.ylabel('Counts')
plt.show()

# Explanation: The Hadamard gate creates a 50-50 chance of measuring |0⟩ or |1⟩.
# In quantum networking, superposition enables parallel processing for protocols
# like quantum key distribution (QKD). Expect ~500 counts each for |0⟩ and |1⟩.
# For research: Experiment with more shots or different gates (e.g., X gate).
```