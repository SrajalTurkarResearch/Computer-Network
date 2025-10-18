# mimo_throughput.py
# Calculates 5G MIMO throughput with multiple antennas
# Purpose: Understand how MIMO scales channel capacity
# Math: C = B * log2(1 + SNR) * min(Nt, Nr), where Nt/Nr are transmit/receive antennas
# Usage: Run to compute and print MIMO throughput

import math


def calculate_mimo_throughput(B, SNR, Nt, Nr):
    """
    Calculate MIMO throughput
    Parameters:
        B (float): Bandwidth (Hz)
        SNR (float): Signal-to-Noise Ratio
        Nt, Nr (int): Number of transmit/receive antennas
    Returns:
        float: Throughput in Gbps
    """
    # Step 1: Base Shannon capacity
    base_C = B * math.log2(1 + SNR)
    # Step 2: MIMO scaling factor
    mimo_factor = min(Nt, Nr)
    # Step 3: Total throughput
    total_C = base_C * mimo_factor / 1_000_000_000  # Convert to Gbps
    return total_C


# Parameters
B = 100_000_000  # 100 MHz bandwidth
SNR = 100  # High SNR for 5G
Nt, Nr = 64, 4  # Massive MIMO setup

# Calculate and print
throughput = calculate_mimo_throughput(B, SNR, Nt, Nr)
print(f"5G MIMO Throughput: {throughput:.2f} Gbps")
# Expected: ~2.66 Gbps (100e6 * log2(101) * 4)
