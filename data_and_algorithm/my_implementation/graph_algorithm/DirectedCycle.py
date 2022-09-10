from data_and_algorithm.my_implementation.graph_algorithm import Graph


class DirectedCycle:
    def __init__(self, graph: Graph.Graph):
        self.graph = graph
        self.on_stack = {i: False for i in self.graph.adj_list}
        self.visited = {i: False for i in self.graph.adj_list}
        self.has_cycle = False
        for key in self.graph.adj_list:
            if not self.visited[key]:
                self.dfs(key)

    def dfs(self, v):
        self.on_stack[v] = True
        self.visited[v] = True
        for i in self.graph.adj(v):
            if self.has_cycle: return
            if not self.visited[i]:
                self.dfs(i)
            elif self.on_stack[i]:
                self.has_cycle = True
        self.on_stack[v] = False

    def has_cycle(self):
        return self.has_cycle
