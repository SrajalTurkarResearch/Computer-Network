# Physical Layer Cheatsheet: Signal Theory, Shannon’s Capacity, Modulation Techniques

This cheatsheet summarizes key concepts, formulas, and insights from the Physical Layer tutorial, designed for quick reference as you build your scientific career. Organized for clarity, it’s ideal for note-taking and review, covering fundamentals, math, visualizations, and research pointers.

## 1. Physical Layer Overview

- **Role** : Converts bits (0s/1s) into physical signals (electrical, optical, radio) for transmission over media (copper, fiber, air).
- **Key Components** : Signals, media, hardware (e.g., transceivers), standards (e.g., IEEE 802.3).
- **Challenges** : Noise, attenuation, interference, propagation delay.
- **Visualization** : OSI model as a 7-layer pyramid, Physical Layer at base. Draw arrows for bit-to-signal conversion.

## 2. Signal Theory

### Core Concepts

- **Signal Types** :
- **Analog** : Continuous (e.g., voice wave).
- **Digital** : Discrete (e.g., binary 0/1).
- **Properties** :
- **Amplitude (A)** : Signal strength (e.g., volts).
- **Frequency (f)** : Cycles per second (Hz).
- **Period (T)** : ( T = 1/f ).
- **Phase (φ)** : Wave shift (radians).
- **Bandwidth (B)** : Frequency range (e.g., 2.4–2.4835 GHz for Wi-Fi).
- **Wavelength (λ)** : ( \lambda = c/f ), where ( c ) is wave speed.
- **Challenges** :
- **Noise** : Random distortion (e.g., static).
- **Attenuation** : Signal loss over distance.
- **Interference** : Signal overlap (e.g., Wi-Fi vs. microwave).
- **Signal-to-Noise Ratio (SNR)** :
  [ SNR_{dB} = 10 \log_{10} \left( \frac{P_{signal}}{P_{noise}} \right) ], where ( P = A^2/2 ).

### Key Formula

- Sine wave:
  [ s(t) = A \sin(2\pi f t + \phi) ]
- Fourier Transform: Decomposes signal into frequencies:
  [ S(f) = \int s(t) e^{-j2\pi f t} dt ]

### Visualization

- **Sine Wave** : Plot amplitude vs. time, label A, T, φ.
- **Digital Signal** : Step plot for 0s/1s.
- **Spectrum** : Amplitude vs. frequency, showing bandwidth.

### Research Note

- Fourier analysis is critical for compression (JPEG, MP3) and signal detection (e.g., gravitational waves).

## 3. Shannon’s Capacity

### Core Concept

- Maximum error-free data rate (C, in bps) over a noisy channel.
- Formula:
  [ C = B \log_2 (1 + SNR) ]
  - ( B ): Bandwidth (Hz).
  - ( SNR ): Linear ratio (( SNR = 10^{SNR\_{dB}/10} )).
- **Nyquist Rate** (noiseless): ( R = 2B \log_2 M ), where ( M ) is signal levels.

### Example

- B = 1 MHz, SNR = 20 dB (( SNR = 10^{20/10} = 100 )):
  [ C = 10^6 \times \log_2(1 + 100) \approx 6.66 \text{ Mbps} ].

### Visualization

- Plot C/B (bits/s/Hz) vs. SNR (dB): Logarithmic curve.
- Compare C for different B values.

### Research Note

- Approaching Shannon’s limit requires advanced coding (e.g., LDPC, polar codes). Explore quantum channels for surpassing classical limits.

## 4. Modulation Techniques

### Core Concepts

- **Modulation** : Alters carrier signal to encode data.
- **Analog** :
- **AM** : Vary amplitude.
- **FM** : Vary frequency.
- **PM** : Vary phase.
- **Digital** :
- **ASK** : Discrete amplitudes.
- **FSK** : Discrete frequencies.
- **PSK** : Discrete phases (e.g., BPSK: 0°=0, 180°=1).
- **QAM** : Combines amplitude and phase (e.g., 16-QAM: 4 bits/symbol).
- **Bit Rate** : ( R_b = R_s \log_2 M ), where ( R_s ) is symbol rate, ( M ) is number of symbols.

### Key Formulas

- Carrier:
  [ c(t) = A_c \sin(2\pi f_c t + \phi_c) ]
- AM: ( s(t) = (1 + m(t)) c(t) ), where ( m(t) ) is message.
- FM: ( s(t) = A_c \sin(2\pi f_c t + k_f \int m(t) dt) ).

### Visualization

- **AM** : Plot carrier with varying envelope.
- **FM** : Plot constant amplitude, varying wavelength.
- **QAM Constellation** : Grid with points (e.g., 16-QAM: 4x4 grid, label bits).

### Research Note

- OFDM (used in Wi-Fi/5G) splits bandwidth into subcarriers. Explore NOMA for 6G.

## 5. Quick-Reference Examples

- **Signal** : 5 Hz sine wave, A=3, add noise with σ=0.5.
- **Capacity** : B=5 MHz, SNR=25 dB → C ≈ 29.86 Mbps.
- **Modulation** : 16-QAM → 4 bits/symbol, needs high SNR.

## 6. Exercises

1. Calculate SNR for signal power 100 W, noise 1 W.
   _Solution_ : ( SNR = 10 \log\_{10}(100/1) = 20 \text{ dB} ).
2. Compute C for B=10 MHz, SNR=15 dB.
3. Sketch AM for bits [1, 0, 1]. Label envelope changes.
4. Research: How does modulation affect IoT battery life?

## 7. Research Directions

- **Signal Theory** : Non-linear signal processing for neural networks.
- **Capacity** : Quantum channels to exceed Shannon’s limit.
- **Modulation** : AI-driven adaptive modulation for 6G.
- **Experiment** : Simulate a 5G link in Python, varying SNR and modulation.

## 8. What’s Missing in Standard Tutorials

- **Non-Gaussian Noise** : Real channels (e.g., fading) require advanced models.
- **Quantum Effects** : Photon-based communication for future networks.
- **Ethical Considerations** : Signal jamming and privacy in wireless systems.

## 9. Visual Aids for Notes

- **OSI Model** : 7-layer stack, Physical Layer at bottom.
- **Signal Spectrum** : Frequency vs. amplitude, highlight bandwidth.
- **Constellation Diagram** : Points for QAM, label bit mappings.
- **Capacity Curve** : C/B vs. SNR, logarithmic growth.

This cheatsheet is your go-to reference. Pair it with the `.py` files and case studies to master the Physical Layer and fuel your scientific journey!
