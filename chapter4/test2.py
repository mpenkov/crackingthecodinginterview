import unittest

import problem2
import digraph


class TestPathExists(unittest.TestCase):

    def setUp(self):
        self.g = digraph.DirectedGraph(range(6))

        self.g.add_edge(0, 1)
        self.g.add_edge(0, 2)
        self.g.add_edge(0, 4)
        self.g.add_edge(2, 3)
        self.g.add_edge(3, 4)
        self.g.add_edge(4, 0)

    def test(self):
        self.assertEquals(problem2.path_exists(self.g, 0, 1), True)
        self.assertEquals(problem2.path_exists(self.g, 0, 2), True)
        self.assertEquals(problem2.path_exists(self.g, 0, 4), True)
        self.assertEquals(problem2.path_exists(self.g, 0, 3), True)

        self.assertEquals(problem2.path_exists(self.g, 2, 0), True)

        self.assertEquals(problem2.path_exists(self.g, 1, 0), False)
        self.assertEquals(problem2.path_exists(self.g, 5, 1), False)
        self.assertEquals(problem2.path_exists(self.g, 5, 4), False)
