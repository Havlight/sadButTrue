from queue import LifoQueue

from data_and_algorithm.my_implementation.graph_algorithm import Graph


class DFS:
    def __init__(self, graph: Graph.Graph, start: int = 0):
        self.reverse_post = LifoQueue()
        self.graph = graph
        self.visited = {i: False for i in self.graph.adj_list.keys()}
        self.edge_to = {i: i for i in self.graph.adj_list.keys()}
        self.s = start

    def dfs(self, i):
        self.visited[i] = True
        for v in self.graph.adj(i):
            if not self.visited[v]:
                self.edge_to[v] = i
                self.dfs(v)
        self.reverse_post.put(i)

    def has_path_to(self, v):
        return self.visited[v]

    def path_to(self, v):
        if not self.visited[v]:
            return None
        path = []
        x = v
        while x != self.s:
            path.append(x)
            x = self.edge_to[x]
            path.reverse()
        return path

    def get_reverse_post(self):
        li = []
        while not self.reverse_post.empty():
            i = self.reverse_post.get()
            li.append(i)
        return li


if __name__ == '__main__':
    pass