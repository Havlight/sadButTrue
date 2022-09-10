from data_and_algorithm.my_implementation.graph_algorithm import DFS, Graph


class KosarajuSCC:
    def __init__(self, graph: Graph.Graph):
        self.graph = graph
        self.visited = {i: False for i in self.graph.adj_list}
        self.id = dict()
        self.cnt = 0
        dfs_order = DFS.DFS(self.graph.reverse())
        for i in dfs_order.graph.adj_list:
            if not dfs_order.visited[i]:
                dfs_order.dfs(i)
        order = dfs_order.get_reverse_post()

        for v in order:
            if not self.visited[v]:
                self.dfs(v)
                self.cnt += 1

    def dfs(self, v):
        self.visited[v] = True
        self.id[v] = self.cnt
        for i in self.graph.adj(v):
            if not self.visited[i]:
                self.dfs(i)

    def storonly_connected(self, v, w):
        return self.id[v] == self.id[w]

    def get_id(self, v):
        return self.id[v]


if __name__ == '__main__':
    li = [(0, 5), (0, 1), (2, 0), (6, 0), (3, 2), (2, 3), (3, 5), (5, 4), (4, 3), (4, 2), (6, 4), (6, 9), (11, 4),
          (11, 12), (10, 12), (9, 10), (9, 11), (12, 9)
        , (7, 6), (7, 8), (8, 7), (8, 9)]
    g = Graph.Graph(is_weighted=False, li=li)

    k = KosarajuSCC(g)
    print(k.storonly_connected(2, 3))
