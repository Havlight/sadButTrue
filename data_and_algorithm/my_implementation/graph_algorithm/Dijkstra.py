import sys

from data_and_algorithm.my_implementation.graph_algorithm.Graph import Graph
from queue import PriorityQueue


class Dijkstra:
    def __init__(self, graph: Graph, start: int):
        self.graph = graph
        self.start = start
        self.dist_to = {i: sys.maxsize for i in self.graph.adj_list}
        self.visited = {i: False for i in self.graph.adj_list}
        self.pq = PriorityQueue()
        self.edge_to = {start: start}
        self.mst = []

        self.dist_to[start] = 0
        self.pq.put((0, self.start))

        while not self.pq.empty():
            _, v = self.pq.get()
            if self.visited[v]: continue
            self.dijkstra(v)

    def dijkstra(self, v):
        self.visited[v] = True
        self.mst.append((self.edge_to[v], v))

        for i in self.graph.adj(v):
            if self.dist_to[i] > self.dist_to[v] + self.graph.get_weight(v, i):
                self.dist_to[i] = self.dist_to[v] + self.graph.get_weight(v, i)
                self.edge_to[i] = v
                self.pq.put((self.dist_to[i], i))

    def get_mst(self):
        return self.mst

    def has_path_to(self, v):
        return self.dist_to[v] < sys.maxsize

    def path_to(self, v):
        if not self.has_path_to(v):
            return
        path = []
        p = self.edge_to[v]
        while p != self.start:
            path.append(p)
            p = self.edge_to[p]
        path.append(self.start)
        path.reverse()
        return path


if __name__ == '__main__':
    li = [(1, 3, 3), (1, 2, 7), (1, 4, 11), (2, 1, 5), (3, 2, 2), (2, 5, 2), (4, 5, 3), (2, 4, 4)]
    g = Graph(li=li)
    d = Dijkstra(g, 1)
    print(d.path_to(5))
