# AI in Networking Cheatsheet: Traffic Prediction and Anomaly Detection

This cheatsheet is your quick reference for mastering AI in networking, tailored for aspiring scientists. It summarizes key concepts, formulas, code snippets, and tips from the comprehensive tutorial. Use it for revision, note-taking, or quick lookups while experimenting. All terms are explained simply, and calculations are open for clarity.

---

## 1. Fundamentals of Computer Networks

- **Definition**: A web of devices (nodes) connected by links (wired/wireless) to share data.
- **Components**:
  - **Nodes**: Computers, routers, servers.
  - **Links**: Cables, Wi-Fi.
  - **Protocols**: Rules (e.g., TCP/IP).
- **OSI Model** (7 Layers):
  - Physical (bits), Data Link (frames), Network (packets), Transport (segments), Session, Presentation, Application.
- **Traffic Metrics**:
  - **Bandwidth**: Data capacity (Mbps).
  - **Latency**: Delay (ms).
  - **Jitter**: Delay variation, \( J = \sqrt{\frac{\sum (d_i - \bar{d})^2}{n}} \).
  - **Throughput**: Data rate.
- **Queue Model (M/M/1)**:
  - Utilization: \( \rho = \lambda / \mu \) (arrival rate / service rate).
  - Delay: \( D = 1 / (\mu - \lambda) \).

**Example**: For \(\lambda = 5\), \(\mu = 6\), \(\rho = 5/6\), \(D = 1/(6-5) = 1\) sec.

**Analogy**: Network = highway, packets = cars, routers = traffic lights.

---

## 2. AI and Machine Learning Basics

- **AI**: Computers acting smart, mimicking human decisions.
- **ML**: Learning from data without hard-coded rules.
- **Types**:
  - **Supervised**: Labeled data (e.g., predict traffic with known values).
  - **Unsupervised**: No labels (e.g., find anomalies).
  - **Reinforcement**: Learn via rewards (e.g., Q-learning: \( Q = r + \gamma \max Q\_{\text{next}} \)).
- **Pipeline**:
  1. Collect data (e.g., Wireshark).
  2. Preprocess (normalize: \( x' = \frac{x - \min}{\max - \min} \)).
  3. Feature selection (e.g., PCA).
  4. Train model.
  5. Evaluate (e.g., MSE: \( \frac{1}{n} \sum (y_i - \hat{y}\_i)^2 \)).

**Code Snippet (Normalization)**:

````python
from sklearn.preprocessing import MinMaxScaler
scaler = MinMaxScaler()
data_scaled = scaler.fit_transform(data)

Tip: Use cross-validation to avoid overfitting.

3. Traffic Prediction

Goal: Forecast future network traffic (e.g., bandwidth needs).
Models:
ARIMA: Statistical, for linear trends.
LSTM: Neural network for sequences, handles non-linear patterns.
GNN: Captures network topology.


LSTM Math:
Forget Gate: ( f_t = \sigma(W_f [h_{t-1}, x_t] + b_f) ).
Input Gate: ( i_t = \sigma(W_i [h_{t-1}, x_t] + b_i) ).
Cell Update: ( C_t = f_t \cdot C_{t-1} + i_t \cdot \tanh(W_c [h_{t-1}, x_t] + b_c) ).
Output: ( h_t = o_t \cdot \tanh(C_t) ).



Example Calculation:

Input ( x_t = 1 ), ( h_{t-1} = 0 ), weights = 1, bias = 0.
( f_t = \sigma(1) \approx 0.73 ), ( i_t \approx 0.73 ), ( \tanh(1) \approx 0.76 ).
( C_t = 0.73 \cdot 0 + 0.73 \cdot 0.76 \approx 0.55 ).

Code Snippet (LSTM):
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import LSTM, Dense
model = Sequential([LSTM(50, activation='relu', input_shape=(10, 1)), Dense(1)])
model.compile(optimizer='adam', loss='mse')

Tip: Use datasets like CESNET-TimeSeries24 for real-world practice.

4. Anomaly Detection

Goal: Spot unusual traffic (e.g., DDoS attacks).
Models:
Isolation Forest: Splits data randomly; anomalies split faster.
Autoencoder: Reconstructs data; high error = anomaly.


Autoencoder Math:
Encoder: ( z = f(x) ).
Decoder: ( \hat{x} = g(z) ).
Loss: ( ||x - \hat{x}||^2 ).
Threshold: Mean + 3*std of normal errors.



Example Calculation:

Input ( x = [1, 2] ), reconstructed ( \hat{x} = [1.4, 2.1] ).
Error: ( (1-1.4)^2 + (2-2.1)^2 = 0.16 + 0.01 = 0.17 ).

Code Snippet (Autoencoder):
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
autoencoder = Sequential([
    Dense(2, activation='relu', input_shape=(5,)),
    Dense(5, activation='sigmoid')
])
autoencoder.compile(optimizer='adam', loss='mse')

Tip: Test on NSL-KDD dataset for intrusion detection.

5. Visualizations

Network Topology (Star):

import matplotlib.pyplot as plt
fig, ax = plt.subplots()
ax.add_patch(plt.Circle((0.5, 0.5), 0.1, color='red'))  # Hub
for i in range(4):
    angle = i * 90
    x = 0.5 + 0.3 * np.cos(np.radians(angle))
    y = 0.5 + 0.3 * np.sin(np.radians(angle))
    ax.add_patch(plt.Circle((x, y), 0.05, color='blue'))
    ax.plot([0.5, x], [0.5, y], 'k--')
ax.set_title('Star Topology')
plt.show()


Traffic Plot:

import numpy as np
time = np.arange(0, 24, 1)
traffic = 50 + 30 * np.sin(2 * np.pi * time / 24)
plt.plot(time, traffic)
plt.title('Daily Traffic')
plt.show()

Tip: Use Seaborn for prettier plots.

6. Research Directions

Trends (2025):
Graph Neural Networks (GNNs) for spatial-temporal prediction.
Federated Learning for privacy.


Rare Insights:
Quantum ML: Faster predictions for 6G.
Ethics: Avoid bias in anomaly flagging (e.g., fair datasets).


Experiment Ideas:
Combine LSTM and Isolation Forest.
Test on encrypted traffic.




7. Projects

Mini: Predict traffic on Kaggle dataset.df = pd.read_csv('network_traffic.csv')
traffic = df['traffic_volume'].values
# Apply LSTM as above


Major: NSL-KDD anomaly detection.df = pd.read_csv('KDDTrain+.csv', header=None)
normal = df[df.iloc[:, -1] == 'normal'].iloc[:, :-1]
# Train autoencoder



Tip: Download datasets from Kaggle or UNB CIC.

8. Exercises

LSTM Multi-Step:
Modify output to predict 5 steps.
Solution: Change Dense(1) to Dense(5), adjust y shape.


Autoencoder Tuning:
Test encoding_dim = 1, 2, 4.
Solution: Loop and compute F1-score.




9. Future Steps

Learn: GNNs, federated learning.
Tools: Mininet, NS-3 for simulations.
Publish: Aim for IEEE, arXiv.
Ethics: Study bias in ML models.

Tip: Join GitHub for open-source projects.

10. What’s Missing in Standard Tutorials

Scalability: Use Spark for big data.
Explainability: SHAP for model insights.
Privacy: Differential privacy techniques.
Hybrid Models: LSTM + Isolation Forest.

Final Note: Like Einstein’s equations, simplify complex ideas through practice. Experiment with these snippets and datasets to build your scientific intuition!```
````
