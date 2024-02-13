class Node:
    def __init__(self, data=None) -> None:
        self.data = data
        self.left = None
        self.right = None


class Binaryroot:

    def __init__(self) -> None:
        self.tree = None

    def insert(self, data):
        node = Node(data)
        if (self.tree is None):
            self.tree = node
        else:
            current = self.tree
            while True:
                if (data < current.data):
                    if (current.left is None):
                        current.left = node
                        break
                    current = current.left
                if (data > current.data):
                    if (current.right is None):
                        current.right = node
                        break
                    current = current.right

    def bfs(self, root):
        if (root is None):
            return []
        queue = [root]
        values = []
        while (len(queue) > 0):
            current = queue.pop(0)
            values.append(current.data)
            if (current.left):
                queue.append(current.left)
            if (current.right):
                queue.append(current.right)
        return values

    def dfs(self, root):
        if (root is not None):
            stack = [root]
            values = []
            while (len(stack) > 0):
                current = stack.pop()
                values.append(current.data)
                if (current.right):
                    stack.append(current.right)
                if (current.left):
                    stack.append(current.left)
            return values
        return []

    def dfs_recursion(self, root):
        if (root is not None):
            leftVal = []
            rightVal = []
            if (root.left):
                leftVal = self.dfs(root.left)
            if (root.right):
                rightVal = self.dfs(root.right)
            return root.data, leftVal, rightVal
        return []


bst = Binaryroot()

#       15
#     /    \
#    5      43
#   / \    /  \
#  3  14  33   50

bst.insert(15)
bst.insert(5)
bst.insert(3)
bst.insert(43)
bst.insert(33)
bst.insert(50)
bst.insert(14)

bfs = bst.bfs(bst.tree)
dfs = bst.dfs(bst.tree)
dfs_rec = bst.dfs_recursion(bst.tree)

print(bfs)
print(dfs)
print(dfs_rec)
