def buildGraph(edges):
    graph = {}
    for edge in edges:
        [a, b] = edge
        if not (a in graph):
            graph[a] = []
        if not (b in graph):
            graph[b] = []
        graph[a].append(b)
        graph[b].append(a)
    return graph


if __name__ == "__main__":
    edges = [
        ['b', 'a'],
        ['c', 'a'],
        ['b', 'c'],
        ['q', 'r'],
        ['q', 's'],
        ['q', 'u'],
        ['q', 't'],
    ]
    graph = buildGraph(edges)
    print(graph)
