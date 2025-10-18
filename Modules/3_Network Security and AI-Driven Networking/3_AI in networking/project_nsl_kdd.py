"""
project_nsl_kdd.py

Implements anomaly detection on the NSL-KDD dataset using an autoencoder.
Researchers can adapt this for intrusion detection studies.
Note: Requires NSL-KDD dataset (download from https://www.unb.ca/cic/datasets/nsl.html).

Dependencies: numpy, pandas, scikit-learn, tensorflow, matplotlib
Run: python project_nsl_kdd.py (after downloading and specifying dataset path)
"""

import numpy as np
import pandas as pd
from sklearn.preprocessing import MinMaxScaler
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, RepeatVector, TimeDistributed
import matplotlib.pyplot as plt


def load_nsl_kdd_data(path="KDDTrain+.csv"):
    """
    Load and preprocess NSL-KDD dataset.
    Args:
        path: Path to NSL-KDD training CSV.
    Returns:
        normal_data: Normal samples, all_data: All samples, labels: Attack labels.
    """
    try:
        df = pd.read_csv(path, header=None)
        features = df.iloc[:, :-1].values
        labels = df.iloc[:, -1].values
        normal_data = features[labels == "normal"]
        return normal_data, features, labels
    except FileNotFoundError:
        print(
            f"Error: Dataset not found at {path}. Download from https://www.unb.ca/cic/datasets/nsl.html"
        )
        return None, None, None


def main():
    # Step 1: Load data
    normal_data, all_data, labels = load_nsl_kdd_data()
    if normal_data is None:
        return

    # Step 2: Scale data
    scaler = MinMaxScaler()
    normal_scaled = scaler.fit_transform(normal_data)
    all_data_scaled = scaler.transform(all_data)

    # Step 3: Build Autoencoder
    input_dim = normal_data.shape[1]
    encoding_dim = 10
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

    # Step 6: Set threshold
    threshold = np.mean(mse[: len(normal_data)]) + 3 * np.std(mse[: len(normal_data)])
    anomalies = mse > threshold

    # Step 7: Evaluate (assuming labels indicate anomalies)
    true_anomalies = (labels != "normal").astype(int)
    detected_anomalies = anomalies.astype(int)
    precision = np.sum((detected_anomalies == 1) & (true_anomalies == 1)) / np.sum(
        detected_anomalies
    )
    recall = np.sum((detected_anomalies == 1) & (true_anomalies == 1)) / np.sum(
        true_anomalies
    )
    print(f"Precision: {precision:.2f}, Recall: {recall:.2f}")

    # Step 8: Visualize
    plt.figure(figsize=(10, 4))
    plt.plot(mse, label="Reconstruction Error")
    plt.axhline(threshold, color="r", linestyle="--", label="Threshold")
    plt.title("NSL-KDD Anomaly Detection Scores")
    plt.xlabel("Sample Index")
    plt.ylabel("Mean Squared Error")
    plt.legend()
    plt.show()


if __name__ == "__main__":
    main()
