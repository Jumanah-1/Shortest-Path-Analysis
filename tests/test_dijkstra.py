from math import inf

from algorithms.graph import Graph
from algorithms.dijkstra import dijkstra, reconstruct_path


# Test 1: Shortest distances
graph = Graph(directed=True)

graph.add_edge("A", "B", 4)
graph.add_edge("A", "C", 2)
graph.add_edge("B", "C", 5)
graph.add_edge("C", "D", 3)
graph.add_edge("B", "D", 10)

distances, previous = dijkstra(graph, "A")

assert distances["A"] == 0
assert distances["B"] == 4
assert distances["C"] == 2
assert distances["D"] == 5

print("Test 1: Shortest Distances - PASSED")


# Test 2: Path reconstruction
path = reconstruct_path(previous, "A", "D")

assert path == ["A", "C", "D"]

print("Test 2: Path Reconstruction - PASSED")


# Test 3: Unreachable vertex
graph.add_vertex("E")

distances, previous = dijkstra(graph, "A")

assert distances["E"] == inf
assert reconstruct_path(previous, "A", "E") == []

print("Test 3: Unreachable Vertex - PASSED")


# Test 4: Negative weights
negative_graph = Graph()
negative_graph.add_edge("A", "B", -3)

try:
    dijkstra(negative_graph, "A")
    assert False, "Negative weight was not rejected"
except ValueError:
    print("Test 4: Negative Weights - PASSED")


# Test 5: Invalid starting vertex
try:
    dijkstra(graph, "Z")
    assert False, "Invalid starting vertex was not rejected"
except ValueError:
    print("Test 5: Invalid Start - PASSED")


# Test 6: Start equals destination
distances, previous = dijkstra(graph, "A")

assert reconstruct_path(previous, "A", "A") == ["A"]

print("Test 6: Start Equals Destination - PASSED")


# Test 7: Zero-weight edges
graph = Graph()
graph.add_edge("A", "B", 0)
graph.add_edge("B", "C", 2)
graph.add_edge("A", "C", 5)

distances, previous = dijkstra(graph, "A")

assert distances["B"] == 0
assert distances["C"] == 2
assert reconstruct_path(previous, "A", "C") == ["A", "B", "C"]

print("Test 7: Zero-Weight Edges - PASSED")


# Test 8: Undirected graph
graph = Graph(directed=False)
graph.add_edge("A", "B", 3)
graph.add_edge("B", "C", 4)

distances, previous = dijkstra(graph, "C")

assert distances["A"] == 7
assert reconstruct_path(previous, "C", "A") == ["C", "B", "A"]

print("Test 8: Undirected Graph - PASSED")


# Test 9: Updating shorter distances
graph = Graph()
graph.add_edge("A", "B", 10)
graph.add_edge("A", "C", 2)
graph.add_edge("C", "B", 3)

distances, previous = dijkstra(graph, "A")

assert distances["B"] == 5
assert reconstruct_path(previous, "A", "B") == ["A", "C", "B"]

print("Test 9: Distance Update - PASSED")


# Test 10: Equal-cost paths
graph = Graph()
graph.add_edge("A", "B", 2)
graph.add_edge("A", "C", 2)
graph.add_edge("B", "D", 3)
graph.add_edge("C", "D", 3)

distances, previous = dijkstra(graph, "A")

assert distances["D"] == 5
assert reconstruct_path(previous, "A", "D") in [
    ["A", "B", "D"],
    ["A", "C", "D"]
]

print("Test 10: Equal-Cost Paths - PASSED")


# Test 11: Empty graph
graph = Graph()

try:
    dijkstra(graph, "A")
    assert False, "Empty graph was not rejected"
except ValueError:
    print("Test 11: Empty Graph - PASSED")


print("\nAll 11 Dijkstra tests passed successfully!")