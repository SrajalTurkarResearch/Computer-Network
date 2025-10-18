# Cheat Sheet for Decentralized Networks Tutorial: Blockchain and Consensus Algorithms

This cheat sheet summarizes key concepts, formulas, analogies, and tips from the tutorial. Use it as a quick reference for exams, research, or coding—like Einstein's pocket notes on relativity or Tesla's sketches of AC motors. Organized by section for easy navigation.

## Section 1: Foundations

- **Network Types**:
  - Centralized: Single point (analogy: monarchy); pros: simple; cons: failure-prone. Reliability: p (one node).
  - Decentralized: Multiple hubs (analogy: federation); reliability: 1 - (1-p)^k.
  - Distributed: All equal (analogy: democracy); uses P2P.
- **Graph Theory Basics**: G = (V, E); degree = connections. Min edges for connected: n-1.
- **Cryptography Essentials**:
  - Hash: SHA-256(input) → 64-char hex (one-way).
  - Asymmetric: Public/private keys; math: ECC (y² = x³ + ax + b mod p).
- **Tip**: Sketch graphs to visualize—centralized as star, distributed as mesh.

## Section 2: Decentralized Networks

- **Challenges**: CAP Theorem (pick 2: Consistency, Availability, Partition tolerance).
- **Byzantine Problem**: Tolerate f faults with 3f+1 nodes.
- **Analogy**: Generals agreeing despite traitors.
- **Math**: Quorum = floor(n/2) + 1.

## Section 3: Blockchain

- **Structure**: Chain of blocks; each: header (prev_hash, merkle_root, nonce) + transactions.
- **Hashing**: h(data) collision-resistant; change 1 bit → new hash.
- **Mining (PoW)**: Find nonce where h(block) < target; tries ≈ 2^difficulty.
- **Merkle Tree**: Root = h(h(left) + h(right)); verify in O(log n).
- **Properties**: Immutability, transparency.
- **Variants**: PoS (stake-based); permissioned (private).
- **Attacks**: 51% (control >50% power); prob success = (q/p)^k where q=attacker power.
- **Tip**: Simulate with Python: Use hashlib for hashes.

## Section 4: Consensus Algorithms

- **Properties**: Safety (no wrong), Liveness (eventual agreement).
- **FLP Impossibility**: No perfect consensus in async with failures—use timeouts.
- **Paxos**:
  - Roles: Proposers, acceptors, learners.
  - Phases: Prepare (promise n), Accept (if majority).
  - Tolerates: f crashes in 2f+1.
  - Analogy: Auction with bids.
- **Raft**:
  - States: Leader, follower, candidate.
  - Election: Random timeout, majority votes.
  - Log Replication: Leader appends, commits on majority ack.
  - Math: Term monotonic; commit index advances.
  - Analogy: Classroom vote.
- **PBFT**: For Byzantine; 3f+1 nodes, 3 phases.
- | **Comparison**: | Algo      | Faults | Complexity  | Use |
  | --------------- | --------- | ------ | ----------- | --- |
  | Paxos           | Crash     | High   | Google      |
  | Raft            | Crash     | Low    | etcd        |
  | PBFT            | Byzantine | Medium | Hyperledger |
- **Tip**: Implement Raft first—easier to debug.

## Section 5: Advanced & Research

- **Scalability**: Sharding (divide data), Layer-2 (off-chain).
- **Quantum Threats**: Use lattice crypto.
- **Ethics**: Energy (PoW), inequality (PoS).
- **Future**: AI-consensus hybrids; DeSci for research.
- **Project Ideas**: Simulate 51% attack; build DAO.
- **What's Missing in Tutorials**: Overlook ethics, quantum risks—always question assumptions like Einstein.

Memorize key math for proofs; experiment with code for intuition. Reference full tutorial for details. Onward to discovery!
