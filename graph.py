from vertex import Vertex


class Graph:

    def __init__(self):
        self.vertexes = {}

    def __str__(self):
        keys = []
        for key in self.vertexes:
            keys.append(key)
        return str(keys)

    def add_vertex(self, id):
        self.vertexes[id] = Vertex(id)

    def add_edge(self, id1, id2):
        if id1 in self.vertexes.keys() and id2 in self.vertexes.keys():
            vertex1 = self.vertexes[id1]
            vertex2 = self.vertexes[id2]
            vertex1.add_neighbor(vertex2)

        else:
            raise Exception('The vertex is not in your graph.')

    def delete_vertex(self, id):
        if id in self.vertexes.keys():
            vertex = self.vertexes[id]
            vertex.delete_neighbors()
            self.vertexes.pop(id)

        else:
            raise Exception('The vertex is not in your graph.')
