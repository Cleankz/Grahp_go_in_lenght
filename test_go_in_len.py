import unittest
import random
from G_in_len import Vertex,SimpleGraph

class MyTests(unittest.TestCase):

    def test_DepthFirstSearch(self):
        graff = SimpleGraph(5)
        edges  = [[],[],[],[],[]]
        search = [[],[],[],[],[]]
        for i in range(5):
            graff.AddVertex(i)
        for i in range(5):
            a = random.randint(0,4)
            b = random.randint(0,4)
            edges[i].append(a)
            edges[i].append(b)
            graff.AddEdge(a,b)
        for i in range(5):
            a = random.randint(0,4)
            b = random.randint(0,4)
            search[i].append(a)
            search[i].append(b)
            print(graff.BreadthFirstSearch(a,b))
    def test_DFS(self):
        graff = SimpleGraph(5)
        graff.AddVertex(0)
        graff.AddVertex(1)
        graff.AddVertex(2)
        graff.AddVertex(3)
        graff.AddVertex(4)
        graff.AddEdge(4, 3)
        graff.AddEdge(2, 3)
        graff.AddEdge(4, 3)
        graff.AddEdge(4, 1)
        graff.AddEdge(0, 2)
        print(graff.DepthFirstSearch(1, 3))


if __name__ == '__main__':
    unittest.main()