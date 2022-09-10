from data_and_algorithm.my_implementation.graph_algorithm import Graph
from queue import Queue


class BFS:
    def __init__(self, graph: Graph.Graph, start):
        self.graph = graph
        self.s = start
        self.visited = {i: False for i in self.graph.adj_list}
        self.edge_to = dict()
        self.qu = Queue()
        self.bfs(self.s)

    def bfs(self, v):
        self.visited[v] = True
        self.qu.put(v)

        while not self.qu.empty():
            i = self.qu.get()
            for j in self.graph.adj(i):
                if not self.visited[j]:
                    self.edge_to[j] = i
                    self.visited[j] = True
                    self.qu.put(j)

    def has_path_to(self, v):
        return self.visited[v]

    def path_to(self, v):
        if not self.has_path_to(v):
            return None
        x = v
        li = []
        while x != self.s:
            li.append(x)
            x = self.edge_to[x]
        li.reverse()
        return li

if __name__ == '__main__':
    b = BFS(Graph.directed_g, 5)
    print(b.path_to(2))