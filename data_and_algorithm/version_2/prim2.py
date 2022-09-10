graph = {
    0: {1: 4, 7: 8},
    1: {2: 8, 7: 11},
    2: {8: 2, 5: 4, 3: 7},
    3: {4: 9, 5: 14},
    4: {5: 10},
    5: {6: 2},
    6: {7: 1, 8: 6},
    7: {8: 7}
}


def init_edges(graph):
    edges = []
    for i in graph.keys():
        for j in graph[i].keys():
            edges.append((i, j, graph[i][j]))
            edges.append((j, i, graph[i][j]))
    return edges

def prim(graph):
    seen = [list(graph.keys())[0]]
    choice = []
    edges = init_edges(graph)
    seen_edge = []

    while len(seen) <= len(graph.keys()):
        for i in edges:
            if i[0] == seen[-1]:
                seen_edge.append(i)
        seen_edge.sort(key=lambda x: x[-1], reverse=True)
        while 1:
            if seen_edge[-1][1] not in seen:
                seen.append(seen_edge[-1][1])
                choice.append(seen_edge.pop())
                break
            else:
                seen_edge.pop()
    return choice


choice = prim(graph)
