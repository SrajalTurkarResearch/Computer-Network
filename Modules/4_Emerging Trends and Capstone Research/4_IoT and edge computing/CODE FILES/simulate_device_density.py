```python
# simulate_device_density.py
# Purpose: Simulate exponential growth of IoT devices to study scalability.
# Context: In IoT, the number of devices can grow rapidly (e.g., 75 billion by 2025).
# This script models D(t) = D0 * 2^t, where D0 is initial devices, t is years.
# Output: Plot of device count over time.
# Requirements: numpy, matplotlib

import numpy as np
import matplotlib.pyplot as plt

def device_growth(t, D0=100):
    """Calculate number of IoT devices at time t years with initial D0 devices.
    Args:
        t (float): Time in years.
        D0 (int): Initial number of devices.
    Returns:
        float: Number of devices at time t.
    """
    return D0 * (2 ** t)

# Generate data for 5 years
years = np.arange(0, 6)  # 0 to 5 years
devices = [device_growth(t) for t in years]

# Plot the growth
plt.figure(figsize=(8, 5))
plt.plot(years, devices, 'b-o', label='Device Growth (D0=100)')
plt.xlabel('Years')
plt.ylabel('Number of Devices')
plt.title('IoT Device Scalability: Exponential Growth')
plt.legend()
plt.grid(True)
plt.show()
```