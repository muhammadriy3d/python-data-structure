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

    print("iterative:")
    depthFirstPrint(graph(), "a")
    print()

    print("Breadth first search:")
    breadthFirstPrint(graph(), "a")
    print()

    print("Breadth first search with target:")
    bfs = breadthFirstSearch(pathGraph(), "f", "k")
    print(bfs)
    print()

    print("Depth first search with target:")
    dfs_rec = depthFirstSearchRecursive(pathGraph(), "f", 'j')
    print(dfs_rec)
    print()

    print("iterative:")
    dfs = depthFirstSearch(pathGraph(), "i", "h")
    print(dfs)


if __name__ == "__main__":
    main()
