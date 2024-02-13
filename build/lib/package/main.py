from linked_list import quick_test
from binary_tree import Binaryroot  

quick_test()

# Binary Search Tree
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
