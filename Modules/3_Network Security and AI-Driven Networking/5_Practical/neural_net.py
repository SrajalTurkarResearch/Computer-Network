# neural_net.py
# Defines a basic neural network for network traffic prediction.
# Illustrates AI in network optimization.

import torch
import torch.nn as nn


# Simple linear neural network class
class Net(nn.Module):
    def __init__(self):
        super().__init__()
        self.fc = nn.Linear(1, 1)  # Single input to single output

    def forward(self, x):
        return self.fc(x)


# Instantiate and print model
model = Net()
print(model)

print("Neural network defined. Train with data for optimization tasks.")
