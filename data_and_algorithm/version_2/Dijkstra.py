import sys

from Graph import generate_graph

a = [('A', 'B', 2), ('B', 'C', 5), ('B', 'D', 6), ('C', 'D', 7), ('E', 'F', 8), ('F', 'C', 9), ('B', 'E', 30)]


def Dijkstra(graph, start):
    visited = {key: False for key in graph}
    path = {key: -1 for key in graph}
    weight_table = {key: graph[start].get(key, sys.maxsize) for key in graph}

    weight_table[start] = 0
    visited[start] = True
    k = int()

    for _ in graph:
        mini = sys.maxsize
        for w in graph:
            if not visited[w] and weight_table[w] < mini:
                k = w
                mini = weight_table[w]
        visited[k] = True
        for w in graph:
            if not visited[w] and (mini + graph[k].get(w, sys.maxsize - mini)) < weight_table[w]:
                weight_table[w] = mini + graph[k].get(w, sys.maxsize - mini)
                path[w] = k
    return weight_table, path


g = generate_graph(a)
# print(g)
print(Dijkstra(g, 'A'))
