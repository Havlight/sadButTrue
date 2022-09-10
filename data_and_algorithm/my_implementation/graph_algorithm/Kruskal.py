from data_and_algorithm.my_implementation.graph_algorithm.Graph import Graph


class Kruskal:
    def __init__(self, graph: Graph):
        self.graph = graph
        self.tree = {i: i for i in self.graph.adj_list}
        self.tree_size = {i: 1 for i in self.graph.adj_list}
        self.edges = self.graph.edges()
        self.mst = []
        for edge in self.edges:
            if len(self.edges) - 1 <= len(self.mst):
                break
            _, m, n = edge
            v = self.find(m)
            w = self.find(n)

            if v != w:
                if self.tree_size[v] < self.tree_size[w]:
                    self.tree[v] = self.tree[w]
                    self.tree_size[w] += self.tree_size[v]
                else:
                    self.tree[w] = self.tree[v]
                    self.tree_size[v] += self.tree_size[w]
                self.mst.append((m, n))

    def find(self, v):
        while v != self.tree[v]:
            v = self.tree[v]
        return v

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
    k = Kruskal(g)
    print(k.get_mst())
# [('B', 'F'), ('C', 'D'), ('C', 'B'), ('C', 'E'), ('A', 'C'), ('C', 'G')]
# [('B', 'F', 1), ('C', 'D', 3), ('C', 'F', 4), ('D', 'E', 4), ('A', 'B', 5), ('A', 'G', 7)]
# [('A', 'A'), ('A', 'B'), ('B', 'F'), ('F', 'C'), ('C', 'D'), ('D', 'E'), ('A', 'G')]