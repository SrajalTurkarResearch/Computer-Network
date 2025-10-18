# routing_algorithms.py
# Implementations of Dijkstra’s and Bellman-Ford algorithms for routing
# For educational and research purposes in Network Layer studies

import heapq


def dijkstra(graph, source):
    """
    Dijkstra’s algorithm for shortest paths in a weighted graph.

    Args:
        graph (dict): Graph as adjacency list {node: {neighbor: weight, ...}}
        source (str): Starting node

    Returns:
        dict: Shortest distances from source to each node
    """
    dist = {node: float("inf") for node in graph}
    dist[source] = 0
    pq = [(0, source)]  # (distance, node)
    while pq:
        d, u = heapq.heappop(pq)
        if d > dist[u]:
            continue
        for v, weight in graph[u].items():
            if dist[u] + weight < dist[v]:
                dist[v] = dist[u] + weight
                heapq.heappush(pq, (dist[v], v))
    return dist


def bellman_ford(graph, source):
    """
    Bellman-Ford algorithm for shortest paths, handles negative weights.

    Args:
        graph (dict): Graph as adjacency list {node: {neighbor: weight, ...}}
        source (str): Starting node

    Returns:
        dict: Shortest distances or raises error if negative cycle detected
    """
    dist = {node: float("inf") for node in graph}
    dist[source] = 0
    # Relax edges |V|-1 times
    for _ in range(len(graph) - 1):
        for u in graph:
            for v, weight in graph[u].items():
                if dist[u] + weight < dist[v]:
                    dist[v] = dist[u] + weight
    # Check for negative cycles
    for u in graph:
        for v, weight in graph[u].items():
            if dist[u] + weight < dist[v]:
                raise ValueError("Graph contains negative cycle")
    return dist


# Example usage
if __name__ == "__main__":
    graph = {"A": {"B": 1, "C": 5}, "B": {"C": 1}, "C": {}}
    print(f"Dijkstra from A: {dijkstra(graph, 'A')}")
    print(f"Bellman-Ford from A: {bellman_ford(graph, 'A')}")
