import sys
from data_and_algorithm.my_implementation.graph_algorithm.Graph import Graph
from queue import PriorityQueue


class Prim:
    def __init__(self, graph: Graph, start):
        self.graph = graph
        self.visited = {i: False for i in self.graph.adj_list}
        self.dist_to = {i: sys.maxsize for i in self.graph.adj_list}
        self.edge_to = {start: start}
        self.pq = PriorityQueue()
        self.mst = []

        self.dist_to[start] = 0
        self.pq.put((0, start))
        while not self.pq.empty():
            self.prim(self.pq.get())

    def prim(self, v):
        v = v[1]
        if self.visited[v]: return
        self.visited[v] = True
        self.mst.append((self.edge_to[v], v))
        for i in self.graph.adj(v):
            if self.visited[i]: continue
            if self.graph.get_weight(v, i) < self.dist_to[i]:
                self.dist_to[i] = self.graph.get_weight(v, i)
                self.edge_to[i] = v
                self.pq.put((self.dist_to[i], i))

    def get_tree(self):
        return self.edge_to

    def get_mst(self):
        return self.mst
if __name__ == '__main__':
    li = [(1, 2, 3), (2, 4, 2), (1, 4, 40), (1, 3, 10), (3, 4, 7), (3, 5, 11), (5, 4, 2)]
    edges = [("A", "B", 5), ("A", "G", 7),
             ("B", "F", 1), ("C", "F", 4),
             ("C", "D", 3), ("C", "E", 7),
             ("E", "F", 6), ("D", "E", 4),
             ("E", "G", 12), ("F", "G", 12)]
    g = Graph(directed=False, li=edges)
    p = Prim(g, 'A')
    print(p.get_mst())
