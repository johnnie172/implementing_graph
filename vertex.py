class Vertex:

    def __init__(self, id):
        self.id = id
        self.neighbors = {}

    def __str__(self):
        vertex_str = "I am " + self.id
        if self.neighbors:
            neighbors_result = ", ".join(self.neighbors.keys())
            vertex_and_neighbors_str = vertex_str + "\nand my neighbors are: " + neighbors_result + "."
        else:
            return  vertex_str
        return vertex_and_neighbors_str

    def add_neighbor(self, neighbor):
        self.neighbors[neighbor.id] = neighbor
        neighbor.neighbors[self.id] = self

    def delete_neighbors(self):
        if not bool(self.neighbors):
            raise Exception("Your vertex have no neighbors.")
        for vertex_id in self.neighbors.keys():
            current_vertex = self.neighbors[vertex_id]
            current_vertex.neighbors.pop(self.id)
        self.neighbors = {}
