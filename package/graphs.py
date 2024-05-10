from numpy import Infinity
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


def largestComponent(graph):
    visited = set()
    largest = 0
    for node in graph:
        size = exploreSize(graph, node, visited)
        if (size > largest):
            largest = size
    return largest


def exploreSize(graph, current, visited):
    if (current in visited):
        return 0
    visited.add(current)
    size = 1
    for neighbors in graph[current]:
        size += exploreSize(graph, neighbors, visited)
    return size


def shortestPath(edges, src, target):
    graph = buildGraph(edges)

    # breadth first is good for this problem for efficiency and easy calculations
    visited = set([src])
    queue = [[src, 0]]
    while (len(queue) > 0):
        [current_node, distance] = queue.pop(0)
        if (current_node is target):
            return distance

        for neighbors in graph[current_node]:
            if not (neighbors in visited):
                visited.add(neighbors)
                queue.append([neighbors, distance + 1])

    return -1


def islandCount(grid):
    visited = set()

    count = 0
    for r in range(len(grid)):
        for c in range(len(grid[0])):
            if (exploreIsland(grid, r, c, visited)):
                count += 1
    return count


def exploreIsland(grid, r, c, visited):
    rowInbounds = 0 <= r and r < len(grid)
    colInbounds = 0 <= c and c < len(grid[0])
    if (not (rowInbounds) or not (colInbounds)):
        return False

    if grid[r][c] == "W":
        return False

    pos = r, ",", c
    if (pos in visited):
        return False
    visited.add(pos)

    exploreIsland(grid, r - 1, c, visited)
    exploreIsland(grid, r + 1, c, visited)
    exploreIsland(grid, r, c - 1, visited)
    exploreIsland(grid, r, c + 1, visited)

    return True


def minIslandSize(grid):
    visited = set()
    size = 0
    min = Infinity

    for r in range(len(grid)):
        for c in range(len(grid[0])):
            size = exploreIslandSize(grid, r, c, visited)
            if (size > 0 and size < min):
                min = size

    return min


def exploreIslandSize(grid, r, c, visited):
    rowInbounds = 0 <= r and r < len(grid)
    colInbounds = 0 <= c and c < len(grid[0])
    if not (rowInbounds) or not (colInbounds):
        return 0

    if grid[r][c] == "W":
        return 0

    pos = r, ",", c
    if pos in visited:
        return 0

    visited.add(pos)

    size = 1
    size += exploreIslandSize(grid, r - 1, c, visited)
    size += exploreIslandSize(grid, r + 1, c, visited)
    size += exploreIslandSize(grid, r, c - 1, visited)
    size += exploreIslandSize(grid, r, c + 1, visited)

    return size


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


def mazeGraph():
    return [
        ['a', 'c'],
        ['a', 'b'],
        ['c', 'b'],
        ['c', 'd'],
        ['b', 'd'],
        ['e', 'd'],
        ['g', 'f']
    ]


def grid():
    return [
        ['W', 'L', 'W', 'W', 'W'],
        ['W', 'L', 'W', 'W', 'W'],
        ['W', 'W', 'W', 'L', 'W'],
        ['W', 'W', 'L', 'L', 'W'],
        ['L', 'W', 'W', 'L', 'L'],
        ['L', 'L', 'W', 'W', 'W'],
    ]


def gridMin():
    return [
        ['W', 'L', 'W', 'W', 'L', 'W'],
        ['L', 'L', 'W', 'W', 'L', 'W'],
        ['W', 'L', 'W', 'W', 'W', 'W'],
        ['W', 'W', 'W', 'L', 'L', 'W'],
        ['W', 'W', 'W', 'L', 'L', 'W'],
        ['W', 'W', 'W', 'L', 'W', 'W'],
    ]


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
    print(ccc)  # excpect 2
    print()

    print("largest component:")
    lc = largestComponent(componentGraph())
    print(lc)
    print()

    print("shortest path:")
    sp = shortestPath(mazeGraph(), 'a', 'e')  # -> 3
    print(sp)
    print()

    print("Island count:")
    ic = islandCount(grid())
    print(ic)
    print()

    print("min Island count size:")
    mics = minIslandSize(gridMin())
    print(mics)
    print()


if __name__ == "__main__":
    main()
