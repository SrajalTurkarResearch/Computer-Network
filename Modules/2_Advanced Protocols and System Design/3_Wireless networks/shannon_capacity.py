# shannon_capacity.py
# Calculates Shannon's Capacity for a wireless channel
# Purpose: Understand maximum data rate given bandwidth and signal-to-noise ratio
# Math: C = B * log2(1 + SNR), where C is capacity (bits/s), B is bandwidth (Hz), SNR is signal-to-noise ratio
# Usage: Run to compute and print capacity for given parameters

import math


def calculate_shannon_capacity(B, SNR):
    """
    Calculate Shannon Capacity
    Parameters:
        B (float): Bandwidth in Hz (e.g., 20e6 for 20 MHz)
        SNR (float): Signal-to-Noise Ratio (unitless)
    Returns:
        float: Capacity in Mbps
    """
    # Step 1: Compute inside the logarithm
    inside_log = 1 + SNR  # Add 1 to SNR for signal-to-noise term
    # Step 2: Compute log base 2
    log_value = math.log2(inside_log)  # log2(1 + SNR)
    # Step 3: Multiply by bandwidth
    C = B * log_value  # Capacity in bits/s
    # Step 4: Convert to Mbps
    C_mbps = C / 1_000_000
    return C_mbps


# Example parameters
B = 20_000_000  # 20 MHz bandwidth
SNR = 15  # SNR of 15 (signal 15x stronger than noise)

# Calculate and print result
capacity = calculate_shannon_capacity(B, SNR)
print(f"Shannon Capacity: {capacity:.2f} Mbps")
# Expected: ~80 Mbps (20e6 * log2(1+15) = 20e6 * 4)
