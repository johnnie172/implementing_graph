import unittest
from graph import Graph

class TestGraph(unittest.TestCase):

    def set_up(self):
        pass

    def test_str(self):
        graph = Graph()
        self.assertEqual(graph.__str__(), '[]')
        graph.add_vertex("tel_aviv")
        self.assertEqual(graph.__str__(), "['tel_aviv']")
        graph.add_vertex("ramat_gan")
        self.assertEqual(graph.__str__(), "['tel_aviv', 'ramat_gan']")



    def test_add_vertex(self):
        graph = Graph()
        graph.add_vertex("tel_aviv")
        vertexes_list = list(graph.vertexes.keys())
        self.assertEqual(vertexes_list[0], "tel_aviv")
        self.assertEqual(len(vertexes_list), 1)
        graph.add_vertex("ramat_gan")
        vertexes_list = list(graph.vertexes.keys())
        self.assertEqual(vertexes_list[0], "tel_aviv")
        self.assertEqual(vertexes_list[1], "ramat_gan")
        self.assertEqual(len(vertexes_list), 2)

    def test_add_edge(self):
        graph = Graph()
        graph.add_vertex("tel_aviv")
        with self.assertRaisesRegex(Exception, 'The vertex is not in your graph.'):
            graph.add_edge("tel_aviv", "ramat_gan")
        graph.add_vertex("ramat_gan")
        graph.add_edge("tel_aviv", "ramat_gan")
        tlv_vertex = graph.vertexes["tel_aviv"]
        rg_vertex = graph.vertexes["ramat_gan"]
        rg_neighbors_list  = list(rg_vertex.neighbors.keys())
        tlv_neighbors_list = list(tlv_vertex.neighbors.keys())
        self.assertEqual(rg_neighbors_list[0], "tel_aviv")
        self.assertEqual(tlv_neighbors_list[0], "ramat_gan")
        graph.add_vertex("savyon")
        graph.add_edge("tel_aviv", "savyon")
        tlv_neighbors_list = list(tlv_vertex.neighbors.keys())
        self.assertEqual(tlv_neighbors_list[1], "savyon")

    def test_delete_vertex(self):
        graph = Graph()
        with self.assertRaisesRegex(Exception, 'The vertex is not in your graph.'):
            graph.delete_vertex("tel_aviv")
        graph.add_vertex("tel_aviv")
        graph.add_vertex("pteh_tikva")
        self.assertEqual(len(graph.vertexes), 2)
        pt_vertex = graph.vertexes["pteh_tikva"]
        graph.add_edge("tel_aviv", "pteh_tikva")
        graph.delete_vertex("tel_aviv")
        self.assertEqual(len(graph.vertexes), 1)
        self.assertEqual(pt_vertex.id, "pteh_tikva")
        with self.assertRaises(KeyError):
            graph.vertexes["tel_aviv"]
        graph.add_vertex("tel_aviv")
        graph.add_vertex("ramat_gan")
        rg_vertex = graph.vertexes["ramat_gan"]
        tlv_vertex = graph.vertexes["tel_aviv"]
        pt_vertex = graph.vertexes["pteh_tikva"]
        graph.add_edge("tel_aviv", "ramat_gan")
        graph.add_edge("pteh_tikva", "ramat_gan")
        self.assertEqual(len(graph.vertexes), 3)
        self.assertEqual(len(rg_vertex.neighbors), 2)
        self.assertEqual(len(pt_vertex.neighbors), 1)
        self.assertEqual(len(tlv_vertex.neighbors), 1)
        graph.delete_vertex("tel_aviv")
        with self.assertRaisesRegex(Exception, 'The vertex is not in your graph.'):
            graph.delete_vertex("tel_aviv")
        self.assertEqual(len(graph.vertexes), 2)
        self.assertEqual(len(rg_vertex.neighbors), 1)
        self.assertEqual(len(pt_vertex.neighbors), 1)





