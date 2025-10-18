"""
traffic_prediction_lstm.py

Implements a Long Short-Term Memory (LSTM) model for network traffic prediction.
Generates synthetic time-series data, trains an LSTM, and visualizes predictions.
Intended for researchers learning AI in networking.

Dependencies: numpy, pandas, matplotlib, scikit-learn, tensorflow
Run: python traffic_prediction_lstm.py
"""

import numpy as np
import matplotlib.pyplot as plt
from sklearn.preprocessing import MinMaxScaler
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import LSTM, Dense
from tensorflow.keras.optimizers import Adam
from sklearn.metrics import mean_squared_error


def generate_synthetic_data(time_steps=1000):
    """Generate synthetic network traffic data (random walk with trend)."""
    np.random.seed(42)
    traffic = np.cumsum(np.random.randn(time_steps)) + 100
    return traffic


def create_sequences(data, seq_length):
    """
    Create sequences for LSTM input.
    Args:
        data: Scaled time-series data.
        seq_length: Number of time steps to look back.
    Returns:
        X: Input sequences, y: Target values.
    """
    X, y = [], []
    for i in range(len(data) - seq_length):
        X.append(data[i : i + seq_length])
        y.append(data[i + seq_length])
    return np.array(X), np.array(y)


def main():
    # Step 1: Generate synthetic data
    time_steps = 1000
    traffic = generate_synthetic_data(time_steps)

    # Step 2: Scale data to 0-1 range
    scaler = MinMaxScaler(feature_range=(0, 1))
    traffic_scaled = scaler.fit_transform(traffic.reshape(-1, 1))

    # Step 3: Create sequences (look back 10 steps)
    seq_length = 10
    X, y = create_sequences(traffic_scaled, seq_length)

    # Step 4: Split into train/test (80-20)
    split = int(0.8 * len(X))
    X_train, X_test = X[:split], X[split:]
    y_train, y_test = y[:split], y[split:]

    # Step 5: Build LSTM model
    model = Sequential(
        [LSTM(50, activation="relu", input_shape=(seq_length, 1)), Dense(1)]
    )
    model.compile(optimizer=Adam(learning_rate=0.001), loss="mse")

    # Step 6: Train model
    history = model.fit(
        X_train, y_train, epochs=20, batch_size=32, validation_split=0.1, verbose=1
    )

    # Step 7: Predict on test set
    y_pred = model.predict(X_test)

    # Step 8: Inverse scale for interpretation
    y_test_inv = scaler.inverse_transform(y_test.reshape(-1, 1))
    y_pred_inv = scaler.inverse_transform(y_pred)

    # Step 9: Evaluate
    mse = mean_squared_error(y_test_inv, y_pred_inv)
    print(f"Mean Squared Error: {mse:.2f}")

    # Step 10: Visualize results
    plt.figure(figsize=(12, 4))

    # Plot training history
    plt.subplot(1, 2, 1)
    plt.plot(history.history["loss"], label="Train Loss")
    plt.plot(history.history["val_loss"], label="Validation Loss")
    plt.title("LSTM Training History")
    plt.xlabel("Epoch")
    plt.ylabel("Loss")
    plt.legend()

    # Plot predictions
    plt.subplot(1, 2, 2)
    plt.plot(y_test_inv[:100], label="Actual Traffic")
    plt.plot(y_pred_inv[:100], label="Predicted Traffic")
    plt.title("Traffic Prediction (First 100 Test Points)")
    plt.xlabel("Time Step")
    plt.ylabel("Traffic Volume")
    plt.legend()

    plt.tight_layout()
    plt.show()


if __name__ == "__main__":
    main()
