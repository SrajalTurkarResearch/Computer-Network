# raft_simulation.py
# Simplified Raft consensus with leader election.

import random


class RaftNode:
    def __init__(self, id, nodes):
        self.id = id
        self.nodes = nodes
        self.state = "follower"
        self.term = 0
        self.voted_for = None

    def election(self):
        self.term += 1
        self.voted_for = self.id
        votes = 1
        for node in self.nodes:
            if node != self and random.choice([True, False]):  # Simulate vote
                votes += 1
        if votes > len(self.nodes) / 2:
            self.state = "leader"


# Example Usage
if __name__ == "__main__":
    nodes = [RaftNode(i, []) for i in range(5)]
    nodes[0].nodes = nodes  # Set nodes list for the first node
    nodes[0].election()
    print(f"Node 0 state after election: {nodes[0].state}")

# To run: python raft_simulation.py
