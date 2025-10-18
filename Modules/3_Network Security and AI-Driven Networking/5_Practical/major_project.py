# major_project.py
# Major project: Autoencoder for anomaly detection in network data.
# Use with datasets like CIC-IDS2018.

import torch
import torch.nn as nn
import torch.optim as optim
import numpy as np


# Autoencoder class
class Autoencoder(nn.Module):
    def __init__(self, input_dim):
        super().__init__()
        self.encoder = nn.Sequential(
            nn.Linear(input_dim, 32), nn.ReLU(), nn.Linear(32, 16)
        )
        self.decoder = nn.Sequential(
            nn.Linear(16, 32), nn.ReLU(), nn.Linear(32, input_dim)
        )

    def forward(self, x):
        return self.decoder(self.encoder(x))


# Sample data (replace with real dataset)
data = np.random.rand(100, 10).astype(np.float32)  # 100 samples, 10 features
input_dim = data.shape[1]

# Model, optimizer, loss
model = Autoencoder(input_dim)
optimizer = optim.Adam(model.parameters(), lr=0.001)
criterion = nn.MSELoss()

# Training loop (simple example)
for epoch in range(10):
    inputs = torch.from_numpy(data)
    outputs = model(inputs)
    loss = criterion(outputs, inputs)
    optimizer.zero_grad()
    loss.backward()
    optimizer.step()
    print(f"Epoch {epoch+1}, Loss: {loss.item():.4f}")

print("Autoencoder trained. Use reconstruction error to detect anomalies.")
