from helpers.buildGraph import buildGraph


def depthFirstPrint(graph, source):
    stack = [source]
    while (len(stack) > 0):
        current = stack.pop()
        print(current)
        for neighbor in graph[current]:
            stack.append(neighbor)


def depthFirstPrintRecursive(graph, source):
    print(source)
    for neighbor in graph[source]:
        depthFirstPrintRecursive(graph, neighbor)


def breadthFirstPrint(graph, source):
    queue = [source]
    while (len(queue) > 0):
        current = queue.pop(0)
        print(current)
        for neighbor in graph[current]:
            queue.append(neighbor)


def breadthFirstSearch(graph, source, target):
    if (source is target):
        return True
    queue = [source]
    while len(queue) > 0:
        current = queue.pop(0)
        if (target is current):
            return True
        for neighbor in graph[current]:
            queue.append(neighbor)
    return False


def depthFirstSearch(graph, source, target):
    if (source == target):
        return True

    stack = [source]
    while len(stack) > 0:
        current = stack.pop()
        if (current == target):
            return True
        for neighbor in graph[current]:
            stack.append(neighbor)
    return False


def depthFirstSearchRecursive(graph, source, target):
    if (source == target):
        return True
    for neighbor in graph[source]:
        if depthFirstSearchRecursive(graph, neighbor, target) == True:
            return True
    return False


def undirectedPath(edges, source, target):
    graph = buildGraph(edges)
    return hasPath(graph, source, target, set())


def hasPath(graph, source, target, visited):
    if (source is target):
        return True
    if source in visited:
        return False

    visited.add(source)

    for neighbor in graph[source]:
        path = hasPath(graph, neighbor, target, visited)
        if path is True:
            return True
    return False


def connectedComponentsCount(graph):
    visited = set()
    nodeCount = 0

    for node in graph:
        path = explore(graph, node, visited)
        if (path):
            nodeCount += 1
    return nodeCount


def explore(graph, current, visited):
    if (current in visited):
        return False

    visited.add(current)

    for neighbor in graph[current]:
        explore(graph, neighbor, visited)

    return True


def undirectedGraph():
    return [
        ['i', 'j'],
        ['k', 'i'],
        ['m', 'k'],
        ['k', 'l'],
        ['o', 'n']
    ]


def componentGraph():
    return {
        0: [8, 1, 5],
        1: [0],
        5: [0, 8],
        8: [0, 5],
        2: [3, 4],
        3: [2, 4],
        4: [3, 2]
    }


def graph():
    return {
        "a": ["b", "c"],
        "b": ["d"],
        "c": ["e"],
        "d": ["f"],
        "e": [],
        "f": []
    }


def pathGraph():
    return {
        "f": ['g', 'i'],
        "g": ['h'],
        "h": [],
        "i": ['g', 'k'],
        "j": ['i'],
        "k": []
    }


def main():
    # Normall item printing in graph
    print("Depth first search:")
    depthFirstPrintRecursive(graph(), "a")
    print()

    print("Depth first search, iterative:")
    depthFirstPrint(graph(), "a")
    print()

    print("Breadth first search:")
    breadthFirstPrint(graph(), "a")
    print()

    print("Breadth first search with target:")
    bfs = breadthFirstSearch(pathGraph(), "f", "k")
    print(bfs)
    print()

    print("Depth first search with target, Recursive:")
    dfs_rec = depthFirstSearchRecursive(pathGraph(), "f", 'j')
    print(dfs_rec)
    print()

    print("Depth first search with target, iterative:")
    dfs = depthFirstSearch(pathGraph(), "i", "h")
    print(dfs)
    print()

    print("Undirected path:")
    ug = undirectedPath(undirectedGraph(), 'j', 'm')
    print(ug)
    print()

    print("connected component count:")
    ccc = connectedComponentsCount(componentGraph())
    print(ccc) # excpect 2
    print()


if __name__ == "__main__":
    main()
