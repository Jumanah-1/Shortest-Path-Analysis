# Dijkstra's Algorithm

## 1. Overview

Dijkstra's algorithm is a greedy algorithm used to find
the shortest paths from a single source vertex to all
other vertices in a weighted graph with non-negative
edge weights.

## 2. Graph Representation

The graph is implemented using an adjacency list.

Supported features:

- Directed graphs.
- Undirected graphs.
- Weighted edges.
- Isolated vertices.
- Negative weights for Bellman-Ford compatibility.

Dijkstra's algorithm rejects graphs containing negative
edge weights.

## 3. Implementation

The implementation uses Python and the following
built-in modules:

- heapq: Min-heap priority queue.
- itertools: Unique insertion ordering.
- math: Infinity representation.

The algorithm maintains:

- A distance dictionary.
- A predecessor dictionary.
- A priority queue.

## 4. Algorithm Steps

1. Initialize all vertex distances to infinity.
2. Set the source vertex distance to zero.
3. Insert the source into the priority queue.
4. Extract the vertex with the smallest distance.
5. Ignore outdated priority queue entries.
6. Relax all neighboring edges.
7. Update distances and predecessors when a shorter
   path is discovered.
8. Repeat until the priority queue is empty.
9. Return the distances and predecessors.

## 5. Path Reconstruction

The reconstruct_path function retrieves the shortest
path by following the predecessor dictionary from
the destination back to the source.

If the destination is unreachable, the function
returns an empty list.

## 6. Complexity Analysis

Let:

- V = Number of vertices.
- E = Number of edges.

### Time Complexity

| Operation | Complexity |
|---|---|
| Vertex initialization | O(V) |
| Negative weight validation | O(E) |
| Edge relaxation | O(E) |
| Priority queue operations | O(E log(E+1)) |

Overall time complexity:

O(V + E log(E+1))

For simple graphs, the commonly used upper bound is:

O((V + E) log V)

### Space Complexity

| Component | Complexity |
|---|---|
| Adjacency list | O(V + E) |
| Distance dictionary | O(V) |
| Predecessor dictionary | O(V) |
| Priority queue | O(E + 1) |
| Path reconstruction | O(V) |

Overall space complexity:

O(V + E)

## 7. Testing and Validation

### Graph Structure Tests

| Test Case | Result |
|---|---|
| Directed graph | PASSED |
| Undirected graph | PASSED |
| Negative weights | PASSED |
| Isolated vertex | PASSED |
| Empty graph | PASSED |
| Duplicate vertex | PASSED |

### Dijkstra Algorithm Tests

| Test Case | Result |
|---|---|
| Shortest distances | PASSED |
| Path reconstruction | PASSED |
| Unreachable vertex | PASSED |
| Negative weights | PASSED |
| Invalid starting vertex | PASSED |
| Start equals destination | PASSED |
| Zero-weight edges | PASSED |
| Undirected graph | PASSED |
| Distance update | PASSED |
| Equal-cost paths | PASSED |
| Empty graph | PASSED |

Total tests: 17
Passed: 17
Failed: 0
Success rate: 100%

## 8. Limitations

- Dijkstra's algorithm does not support negative
  edge weights.
- Unreachable vertices retain an infinite distance.
- Multiple shortest paths may exist with equal costs.
  The implementation returns one valid shortest path.

## 9. Running the Tests

Run the following commands from the project root:

    python -m tests.test_graph
    python -m tests.test_dijkstra

## 10. Integration

The Graph class provides a shared graph structure
for both Dijkstra and Bellman-Ford algorithms.

The Dijkstra function returns:

    distances, previous

The reconstruct_path function returns a list of
vertices representing the shortest path.

Integration with Bellman-Ford and the visualization
interface is pending team coordination.