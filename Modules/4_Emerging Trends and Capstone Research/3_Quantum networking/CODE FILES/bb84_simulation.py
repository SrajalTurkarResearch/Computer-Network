```python
# bb84_simulation.py
# Purpose: Simulate the BB84 quantum key distribution protocol, a cornerstone of
# quantum networking for secure key sharing. Demonstrates how quantum properties
# detect eavesdroppers (Eve).
# Author: Grok, created by xAI
# Date: October 18, 2025
# Requirements: Install matplotlib, seaborn, numpy
# Run: python bb84_simulation.py

# Import libraries
import random
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Set professional plot style
plt.style.use('seaborn')

# BB84 simulation function
def simulate_bb84(n_bits, eve_present=False):
    """
    Simulate BB84 protocol.
    Args:
        n_bits (int): Number of qubits to send.
        eve_present (bool): If True, Eve intercepts with 25% error rate.
    Returns:
        key (list): Shared secret key.
        error_rate (float): Fraction of errors detected.
    """
    alice_bits = [random.randint(0, 1) for _ in range(n_bits)]  # Random bits
    alice_bases = [random.choice(['+', 'x']) for _ in range(n_bits)]  # Rectilinear (+), diagonal (x)
    bob_bases = [random.choice(['+', 'x']) for _ in range(n_bits)]  # Bob’s random bases
    bob_results = []
    errors = 0

    for i in range(n_bits):
        if alice_bases[i] == bob_bases[i]:  # Same basis
            result = alice_bits[i]  # Bob gets correct bit
            if eve_present and random.random() < 0.25:  # Eve causes 25% error
                result = 1 - result  # Flip bit
                errors += 1
            bob_results.append(result)
        else:
            bob_results.append(None)  # Discard mismatch

    # Form key from matching bases
    key = [b for a, b, basis in zip(alice_bits, bob_results, alice_bases) if b is not None]
    error_rate = errors / len(key) if key else 0
    return key, error_rate

# Run simulation
n_bits = 100
key, error_rate = simulate_bb84(n_bits, eve_present=True)

# Output results
print(f"Shared key (first 10 bits): {key[:10]}...")
print(f"Key length: {len(key)}")
print(f"Error rate: {error_rate:.3f}")

# Visualize key length
plt.bar(['Key Length'], [len(key)], color='skyblue')
plt.title('BB84 Key Length with Eavesdropper')
plt.ylabel('Bits')
plt.show()

# Explanation: BB84 uses quantum properties to share keys. If error rate > 0.11,
# suspect eavesdropping. In quantum networking, this ensures secure communication.
# For research: Vary n_bits or Eve’s error rate and analyze key length impact.
```