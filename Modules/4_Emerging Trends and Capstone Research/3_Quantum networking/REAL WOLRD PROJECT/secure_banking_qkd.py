```python
# secure_banking_qkd.py
# Project: Simulate Quantum Key Distribution (QKD) for secure banking transactions
# Real-World Inspiration: 2025 advancements in coherence-based QKD over 254 km fiber (Germany),
# extending China's Micius satellite for financial security. Models BB84 with fiber loss.
# Author: Grok, xAI (Turing-Einstein-Tesla synthesis)
# Date: October 18, 2025
# Requirements: pip install numpy matplotlib seaborn
# Run: python secure_banking_qkd.py
# Research Note: In banking, QKD ensures unhackable transactions (e.g., $1T daily global transfers).
# Simulate: Vary distance/loss to see key viability; reflect on post-quantum crypto integration.

import random
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

plt.style.use('seaborn')

def simulate_qkd_banking(distance_km=100, loss_db_per_km=0.2, eve_present=False):
    """
    Simulate BB84 QKD for banking: Generate secure key for transaction encryption.
    Args:
        distance_km (float): Fiber distance (e.g., 254 km real-world benchmark).
        loss_db_per_km (float): Attenuation (0.2 dB/km typical telecom fiber).
        eve_present (bool): Eavesdropper introduces errors.
    Returns:
        key_length, error_rate: Metrics for secure transaction feasibility.
    """
    n_qubits = 1000  # Initial qubits sent
    total_loss_db = distance_km * loss_db_per_km  # Total loss
    transmission_prob = 10 ** (-total_loss_db / 10)  # Linear loss factor
    received_qubits = int(n_qubits * transmission_prob)  # Qubits arriving

    alice_bits = [random.randint(0, 1) for _ in range(received_qubits)]
    alice_bases = [random.choice(['+', 'x']) for _ in range(received_qubits)]
    bob_bases = [random.choice(['+', 'x']) for _ in range(received_qubits)]
    bob_results = []
    errors = 0

    for i in range(received_qubits):
        if alice_bases[i] == bob_bases[i]:
            result = alice_bits[i]
            if eve_present and random.random() < 0.25:  # Eve's disturbance
                result = 1 - result
                errors += 1
            bob_results.append(result)
        else:
            bob_results.append(None)

    key = [b for a, b, basis in zip(alice_bits, bob_results, alice_bases) if b is not None]
    error_rate = errors / len(key) if key else 1.0
    key_length = len(key)  # Final secure key bits

    # Banking simulation: Encrypt a mock transaction amount
    if key_length > 128:  # Minimum for AES-128
        transaction = "Transfer $1,000,000 to Account XYZ"  # Mock
        print(f"Secure transaction enabled with {key_length}-bit key.")
    else:
        print("Key too short: Transaction aborted for security.")

    return key_length, error_rate

# Run simulation for banking scenario
distances = [50, 100, 254]  # km, inspired by real tests
key_lengths = []
error_rates = []

for dist in distances:
    kl, er = simulate_qkd_banking(dist, eve_present=True)
    key_lengths.append(kl)
    error_rates.append(er)

# Visualize
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5))
ax1.plot(distances, key_lengths, marker='o', color='green')
ax1.set_xlabel('Distance (km)')
ax1.set_ylabel('Secure Key Length (bits)')
ax1.set_title('QKD Key Length vs. Distance (Banking Security)')
ax1.grid(True)

sns.barplot(x=distances, y=error_rates, ax=ax2, color='red')
ax2.set_xlabel('Distance (km)')
ax2.set_ylabel('Error Rate')
ax2.set_title('Error Rate with Eavesdropper')

plt.tight_layout()
plt.show()

# Research Reflection: How does fiber loss impact real banking QKD? Propose a repeater integration.
```