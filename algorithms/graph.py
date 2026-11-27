class Graph:
    def __init__(self, directed=True):
        self.adjacency_list = {}
        self.directed = directed

    def add_vertex(self, vertex):
        if vertex not in self.adjacency_list:
            self.adjacency_list[vertex] = []

    def add_edge(self, source, destination, weight):
        self.add_vertex(source)
        self.add_vertex(destination)

        self.adjacency_list[source].append((destination, weight))

        if not self.directed:
            self.adjacency_list[destination].append((source, weight))

    def get_neighbors(self, vertex):
        return self.adjacency_list.get(vertex, [])

    def get_vertices(self):
        return list(self.adjacency_list.keys())

    def get_edges(self):
        edges = []

        for source, neighbors in self.adjacency_list.items():
            for destination, weight in neighbors:
                edges.append((source, destination, weight))

        return edges