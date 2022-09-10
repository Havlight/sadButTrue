from data_and_algorithm.my_implementation.graph_algorithm.Graph import Graph
from data_and_algorithm.my_implementation.graph_algorithm.DirectedCycle import DirectedCycle
from data_and_algorithm.my_implementation.graph_algorithm.DFS import DFS


class Topological:
    def __init__(self, graph: Graph):
        self.graph = graph
        self.order = None
        self.cycle_finder = DirectedCycle(self.graph)
        if not self.cycle_finder.has_cycle():
            s = list(self.graph.adj_list)[0]
            dfs = DFS(self.graph, s)
            self.order = dfs.reverse_post

    def get_order(self):
        return self.order

    def is_DAG(self):
        return self.order != None
