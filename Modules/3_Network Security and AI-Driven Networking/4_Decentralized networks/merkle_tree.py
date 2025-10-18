# merkle_tree.py
# Implementation of a simple Merkle tree for transaction verification.

import hashlib


def merkle_root(transactions):
    if len(transactions) == 1:
        return hashlib.sha256(transactions[0].encode()).hexdigest()
    new_level = []
    for i in range(0, len(transactions), 2):
        left = transactions[i]
        right = transactions[i + 1] if i + 1 < len(transactions) else left
        combined = left + right
        new_level.append(hashlib.sha256(combined.encode()).hexdigest())
    return merkle_root(new_level)


# Example Usage
if __name__ == "__main__":
    root = merkle_root(["tx1", "tx2", "tx3", "tx4"])
    print(f"Merkle Root: {root}")

# To run: python merkle_tree.py
