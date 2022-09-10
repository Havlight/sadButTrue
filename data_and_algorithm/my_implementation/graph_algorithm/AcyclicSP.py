import sys

from data_and_algorithm.my_implementation.graph_algorithm.Graph import Graph
from data_and_algorithm.my_implementation.graph_algorithm.Topological import Topological


class AcyclicSP:
    def __init__(self, g: Graph, s):
        self.g = g
        self.edge_to = {}
        self.dist_to = {i: sys.maxsize for i in self.g.adj_list}
        # self.visited = {i: False for i in self.g.adj_list}

        self.dist_to[s] = 0
        self.top = Topological(self.g)

        for v in self.top.order:
            self.relax(v)

    def relax(self, v):
        for i in self.g.adj(v):
            if self.dist_to[i] > self.dist_to[v] + self.g.get_weight(v, i):
                self.dist_to[i] = self.dist_to[v] + self.g.get_weight(v, i)
                self.edge_to[i] = v

    def get_dist_to(self, v):
        return self.dist_to[v]
