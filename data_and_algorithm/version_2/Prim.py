import sys


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


a = [('A', 'B', 2), ('B', 'C', 5), ('B', 'D', 6), ('C', 'D', 7), ('E', 'F', 8), ('F', 'C', 9), ('B', 'E', 30)]

g = generate_graph(a)


def prim(graph: dict, first):
    adjvex = {i: 0 for i in graph.keys()}
    lowcost = {i: sys.maxsize for i in graph.keys()}
    edges = []
    lowcost[first] = 0
    adjvex[first] = first
    for key in graph:
        lowcost[key] = graph[first].get(key, sys.maxsize)
        adjvex[first] = 0
    for _ in graph:
        mini = sys.maxsize
        k = int()
        for key in graph:
            if lowcost[key] != 0 and lowcost[key] < mini:
                mini = lowcost[key]
                k = key
        if adjvex[k] != 0:
            edges.append((adjvex[k], k, graph[adjvex[k]].get(k)))
        print(adjvex[k], k)
        lowcost[k] = 0
        for key in graph:
            if lowcost[key] != 0 and graph[k].get(key, sys.maxsize) < lowcost[key]:
                lowcost[key] = graph[k].get(key, sys.maxsize)
                adjvex[key] = k
    return lowcost, adjvex, edges


cost, vex, edge = prim(g, 'C')
print(generate_graph(edge))
