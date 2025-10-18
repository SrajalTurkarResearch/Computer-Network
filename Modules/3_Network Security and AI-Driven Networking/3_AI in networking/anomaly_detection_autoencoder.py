"""
anomaly_detection_autoencoder.py

Implements an autoencoder for network anomaly detection using synthetic multivariate data.
Trains on normal data, detects anomalies via reconstruction error, and visualizes results.
Designed for researchers exploring ML-based anomaly detection in networking.

Dependencies: numpy, matplotlib, scikit-learn, tensorflow
Run: python anomaly_detection_autoencoder.py
"""

import numpy as np
import matplotlib.pyplot as plt
from sklearn.preprocessing import MinMaxScaler
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, RepeatVector, TimeDistributed


def generate_synthetic_data():
    """Generate synthetic multivariate network data (normal and anomalous)."""
    np.random.seed(42)
    normal_data = np.random.normal(100, 10, (800, 5))  # 800 normal samples, 5 features
    anomaly_data = np.random.normal(200, 20, (200, 5))  # 200 anomalous samples
    all_data = np.vstack([normal_data, anomaly_data])
    return all_data, normal_data


def main():
    # Step 1: Generate data
    all_data, normal_data = generate_synthetic_data()

    # Step 2: Scale data
    scaler = MinMaxScaler()
    all_data_scaled = scaler.fit_transform(all_data)
    normal_scaled = all_data_scaled[:800]

    # Step 3: Build Autoencoder
    input_dim = 5
    encoding_dim = 2
    autoencoder = Sequential(
        [
            Dense(encoding_dim, activation="relu", input_shape=(input_dim,)),
            RepeatVector(input_dim),
            TimeDistributed(Dense(encoding_dim, activation="relu")),
            TimeDistributed(Dense(1, activation="sigmoid")),
        ]
    )
    autoencoder.compile(optimizer="adam", loss="mse")

    # Step 4: Train on normal data
    autoencoder.fit(normal_scaled, normal_scaled, epochs=50, batch_size=32, verbose=1)

    # Step 5: Compute reconstruction errors
    reconstructions = autoencoder.predict(all_data_scaled)
    mse = np.mean(np.power(all_data_scaled - reconstructions, 2), axis=1)

    # Step 6: Set threshold (mean + 3*std of normal errors)
    threshold = np.mean(mse[:800]) + 3 * np.std(mse[:800])
    anomalies = mse > threshold

    # Step 7: Print results
    print(f"Detected {np.sum(anomalies)} anomalies out of {len(anomalies)} samples.")
    print(f"Threshold: {threshold:.4f}")

    # Step 8: Visualize
    plt.figure(figsize=(10, 4))
    plt.plot(mse, label="Reconstruction Error")
    plt.axhline(threshold, color="r", linestyle="--", label="Threshold")
    plt.title("Anomaly Detection Scores")
    plt.xlabel("Sample Index")
    plt.ylabel("Mean Squared Error")
    plt.legend()
    plt.show()


if __name__ == "__main__":
    main()
