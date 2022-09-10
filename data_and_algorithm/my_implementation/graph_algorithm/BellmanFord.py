import sys

from data_and_algorithm.my_implementation.graph_algorithm.Graph import Graph
from queue import Queue
from data_and_algorithm.my_implementation.graph_algorithm.DirectedCycle import DirectedCycle


class BellmanFordSP:
    def __init__(self, g: Graph, s: int):
        self.cycle = False
        self.g = g
        self.s = s
        self.q = Queue()
        self.on_q = {i: False for i in self.g.adj_list}
        self.dist_to = {i: sys.maxsize for i in self.g.adj_list}
        self.edge_to = {s: s}
        self.cost = 0

        self.q.put(s)
        self.on_q[s] = True
        self.dist_to[s] = 0
        while not self.q.empty() and not self.has_cycle():
            v = self.q.get()
            self.on_q[v] = False
            self.relax(v)

    def relax(self, v):
        for i in self.g.adj(v):
            if self.dist_to[i] > self.dist_to[v] + self.g.get_weight(v, i):
                self.dist_to[i] = self.dist_to[v] + self.g.get_weight(v, i)
                self.edge_to[i] = v
                if not self.on_q[i]:
                    self.q.put(i)
                    self.on_q[i] = True
            if self.cost % len(self.g) == 0:
                self.find_negative_cycle()
            self.cost += 1

    def find_negative_cycle(self):
        spt = Graph()
        for i, v in self.edge_to.items():
            spt.add_edge(v, i)

        cf = DirectedCycle(spt)

        self.cycle = cf.has_cycle()

    def has_cycle(self):
        return self.cycle
