import numpy as np
from scipy.linalg import solve


def compute_steady_state():
    """
    Compute steady-state probabilities for a two-state Markov chain (Idle/Busy).
    Transition matrix P represents probabilities of staying or switching states.
    Solves π = πP, ∑π = 1 using linear algebra.
    """
    # Define transition matrix: Idle (0), Busy (1)
    P = np.array(
        [[0.8, 0.2], [0.3, 0.7]]  # Idle -> Idle: 0.8, Idle -> Busy: 0.2
    )  # Busy -> Idle: 0.3, Busy -> Busy: 0.7
    print("Transition Matrix:\n", P)

    # Set up system: πP = π, ∑π = 1
    A = np.transpose(P - np.eye(2))  # P^T - I
    A = np.vstack((A, [1, 1]))  # Add ∑π = 1 constraint
    b = np.array([0, 0, 1])  # Right-hand side

    # Solve using least squares for robustness
    pi = np.linalg.lstsq(A, b, rcond=None)[0]
    print("Steady-State Probabilities (Idle, Busy):", pi)


if __name__ == "__main__":
    compute_steady_state()
