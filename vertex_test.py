import unittest
from vertex import Vertex


class TestVertex(unittest.TestCase):

    def setUp(self):
        pass

    def test_str(self):
        tlv = Vertex("tel_aviv")
        pt = Vertex("pteh_tikva")
        rg = Vertex("ramat_gan")
        self.assertEqual(tlv.__str__(), "I am tel_aviv")
        self.assertEqual(pt.__str__(), "I am pteh_tikva")
        self.assertEqual(rg.__str__(), "I am ramat_gan")
        tlv.add_neighbor(pt)
        self.assertEqual(tlv.__str__(), "I am tel_aviv\nand my neighbors are: pteh_tikva.")
        tlv.add_neighbor(rg)
        self.assertEqual(tlv.__str__(), "I am tel_aviv\nand my neighbors are: pteh_tikva, ramat_gan.")

    def test_add_neighbor(self):
        tlv = Vertex("tel_aviv")
        pt = Vertex("pteh_tikva")
        rg = Vertex("ramat_gan")
        tlv.add_neighbor(pt)
        self.assertEqual(tlv.neighbors[pt.id], pt)
        self.assertEqual(pt.neighbors[tlv.id], tlv)
        tlv.add_neighbor(rg)
        self.assertEqual(tlv.neighbors[rg.id], rg)
        self.assertEqual(len(rg.neighbors), 1)
        self.assertEqual(len(pt.neighbors), 1)
        self.assertEqual(len(tlv.neighbors), 2)
        self.assertEqual(rg.neighbors[tlv.id], tlv)

    def test_delete_neighbors(self):
        tlv = Vertex("tel_aviv")
        pt = Vertex("pteh_tikva")
        rg = Vertex("ramat_gan")
        with self.assertRaisesRegex(Exception, "Your vertex have no neighbors."):
            pt.delete_neighbors()
        with self.assertRaisesRegex(Exception, "Your vertex have no neighbors."):
            rg.delete_neighbors()
        with self.assertRaisesRegex(Exception, "Your vertex have no neighbors."):
            tlv.delete_neighbors()
        tlv.add_neighbor(pt)
        tlv.add_neighbor(rg)
        self.assertEqual(len(tlv.neighbors), 2)
        tlv.delete_neighbors()
        self.assertEqual(len(tlv.neighbors), 0)