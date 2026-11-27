from algorithms.graph import Graph

# Test 1: Directed Graph
graph = Graph(directed=True)
graph.add_edge("A", "B", 4)
graph.add_edge("A", "C", 2)

assert graph.get_vertices() == ["A", "B", "C"]
assert graph.get_neighbors("A") == [("B", 4), ("C", 2)]
assert graph.get_neighbors("B") == []

print("Test 1: Directed Graph - PASSED")

# Test 2: Undirected Graph
graph = Graph(directed=False)
graph.add_edge("A", "B", 5)

assert graph.get_neighbors("A") == [("B", 5)]
assert graph.get_neighbors("B") == [("A", 5)]

print("Test 2: Undirected Graph - PASSED")

# Test 3: Negative Weights
graph = Graph()
graph.add_edge("A", "B", -3)

assert graph.get_edges() == [("A", "B", -3)]

print("Test 3: Negative Weights - PASSED")

# Test 4: Isolated Vertex
graph = Graph()
graph.add_vertex("X")

assert graph.get_vertices() == ["X"]
assert graph.get_neighbors("X") == []

print("Test 4: Isolated Vertex - PASSED")

# Test 5: Empty Graph
graph = Graph()

assert graph.get_vertices() == []
assert graph.get_edges() == []

print("Test 5: Empty Graph - PASSED")

# Test 6: Duplicate Vertex
graph = Graph()
graph.add_vertex("A")
graph.add_vertex("A")

assert graph.get_vertices() == ["A"]

print("Test 6: Duplicate Vertex - PASSED")

print("\nAll Graph tests passed successfully!")