from data_and_algorithm.my_implementation.graph_algorithm import Graph


class DirectedCycle:
    def __init__(self, graph: Graph.Graph):
        self.graph = graph
        self.visited = {i: False for i in self.graph.adj_list}
        self.has_cycle = False
        for key in self.graph.adj_list:
            if not self.visited[key]:
                self.dfs(key, key)

    def dfs(self, v, u):
        self.visited[v] = True
        for i in self.graph.adj(v):
            if not self.visited[i]:
                self.dfs(i, v)
            elif i != u:
                self.has_cycle = True
                return None

    def has_cycle(self):
        return self.has_cycle
