import sys
from collections import defaultdict


class Graph:
    def __init__(self, directed=True, is_weighted=True, li=None):
        self.adj_list = defaultdict(dict)
        self.directed = directed
        self.is_weighted = is_weighted
        self.size = 0
        if li:
            for i, j, *w in li:
                if not w:
                    w = 0
                else:
                    w = w[0]
                self.add_edge(i, j, w)

    def add_edge(self, f, t, w=0):
        if f not in self.adj_list:
            self.size += 1
            self.adj_list[f] = dict()
        if t not in self.adj_list:
            self.size += 1
            self.adj_list[t] = dict()
        self.adj_list[f][t] = w
        if not self.directed:
            self.adj_list[t][f] = w

    def adj(self, f):
        return self.adj_list[f].keys()

    def get_weight(self, f, t):
        if t not in self.adj_list[f]:
            return sys.maxsize
        return self.adj_list[f][t]

    def edges(self):
        edge_list = []
        if not self.is_weighted:
            for f in self.adj_list.keys():
                for t in self.adj(f):
                    edge_list.append((f, t))
        else:
            for f in self.adj_list.keys():
                for t, w in self.adj_list[f].items():
                    edge_list.append((w, f, t))
            edge_list.sort()
        return edge_list

    def vertex_size(self):
        return self.size

    def reverse(self):
        R = Graph()
        for i in self.adj_list:
            for j in self.adj(i):
                w = self.get_weight(i, j)
                R.add_edge(j, i, w)
        return R

    def __len__(self):
        return len(self.adj_list)

    def __iter__(self):
        return self.adj_list.keys()


if __name__ == '__main__':
    li = [(1, 3), (1, 2), (2, 6), (7, 0), (0, 2), (1, 7), (5, 7), (5, 4), (7, 4), (0, 4), (6, 4), (3, 6), (7, 2),
          (1, 5),
          (0, 6)]
    li2 = [(5, 1), (5, 7), (5, 4), (4, 7), (4, 0), (7, 2), (0, 2), (1, 3), (3, 6), (6, 4), (6, 0), (6, 2), (3, 7)]
    directed_g = Graph(is_weighted=False, li=li2)
    indirected_g = Graph(directed=True, is_weighted=False, li=li)
