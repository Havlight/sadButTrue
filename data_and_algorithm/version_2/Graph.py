import queue


class Vertex:
    def __init__(self, key, tag=None):
        self.key = key
        self.nbrs = {}
        self.visited = False
        self.tag = tag

    def add_nbr(self, adj_key, w=0):
        self.nbrs[adj_key] = w

    def get_key(self):
        return self.key

    def get_nbrs(self):
        return self.nbrs.keys()

    def get_weight(self, w):
        if w in self.nbrs:
            return self.nbrs[w]

    def __str__(self):
        return str(self.key)

    def __hash__(self):
        return hash(self.key)


class Graph:
    def __init__(self, directed=False):
        self.vertex_list = {}
        self.vertex_num = 0
        self.directed = directed

    def add_vertex(self, key):
        self.vertex_list[key] = Vertex(key)
        self.vertex_num += 1

    def add_edge(self, f, t, w=0):
        if f not in self.vertex_list.keys():
            self.add_vertex(f)
        if t not in self.vertex_list.keys():
            self.add_vertex(t)
        self.vertex_list[f].add_nbr(self.vertex_list[t], w)
        if not self.directed:
            self.vertex_list[t].add_nbr(self.vertex_list[f], w)

    def get_nbrs(self, v):
        return self.vertex_list[v].get_nbrs()

    def get_edges(self):
        edges = []
        for i in self:
            for j, w in i.nbrs.items():
                edges.append((i.key, j, w))
        edges.sort(key=lambda edge: edge[2])
        return edges

    def __iter__(self):
        return iter(self.vertex_list.values())

    def get_weight(self, i, j):
        return self.vertex_list[i].get_weight(self.vertex_list[j])

    def dfs(self):
        for vertex in self.vertex_list.values():
            if not vertex.visited:
                self._dfs(vertex)

    def _dfs(self, v: Vertex):
        v.visited = True
        print(v)
        for nbr in v.get_nbrs():
            if not nbr.visited:
                self._dfs(nbr)

    def bfs(self):
        Q = queue.Queue()
        for vertex in self.vertex_list.values():
            if not vertex.visited:
                vertex.visited = True
                print(vertex)
                Q.put(vertex)
                while not Q.empty():
                    v = Q.get()
                    for nbr in v.get_nbrs():
                        if not nbr.visited:
                            nbr.visited = True
                            print(nbr)
                            Q.put(nbr)


def generate_graph(conn, directed=False):
    from collections import defaultdict
    graph = defaultdict(dict)
    for f, t, w in conn:
        if not w:
            w = 0
        graph[f].update({t: w})
        if not directed:
            graph[t].update({f: w})
    return graph
