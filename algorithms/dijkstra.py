import heapq
from itertools import count
from math import inf


def dijkstra(graph, start):
    """
    Find shortest distances and paths from a starting vertex
    using Dijkstra's algorithm.

    Returns:
        distances: Shortest distance from start to each vertex.
        previous: Previous vertex in each shortest path.
    """

    vertices = graph.get_vertices()

    if start not in vertices:
        raise ValueError("Starting vertex does not exist in the graph.")

    # Dijkstra does not support negative edge weights.
    for source, destination, weight in graph.get_edges():
        if weight < 0:
            raise ValueError(
                "Dijkstra cannot process graphs with negative weights."
            )

    # Initialize distances and previous vertices.
    distances = {vertex: inf for vertex in vertices}
    previous = {vertex: None for vertex in vertices}

    distances[start] = 0

    # Priority queue: (distance, insertion_order, vertex)
    # Insertion order avoids comparing vertex labels.
    priority_queue = []
    order = count()

    heapq.heappush(priority_queue, (0, next(order), start))

    while priority_queue:
        current_distance, _, current_vertex = heapq.heappop(
            priority_queue
        )

        # Ignore outdated queue entries.
        if current_distance > distances[current_vertex]:
            continue

        # Relax neighboring edges.
        for neighbor, weight in graph.get_neighbors(current_vertex):

            new_distance = current_distance + weight

            if new_distance < distances[neighbor]:
                distances[neighbor] = new_distance
                previous[neighbor] = current_vertex

                heapq.heappush(
                    priority_queue,
                    (new_distance, next(order), neighbor)
                )

    return distances, previous


def reconstruct_path(previous, start, destination):
    """
    Reconstruct the shortest path from start to destination.
    Returns an empty list if the destination is unreachable.
    """

    if start not in previous or destination not in previous:
        return []

    path = []
    current = destination

    while current is not None:
        path.append(current)

        if current == start:
            return list(reversed(path))

        current = previous[current]

    return []