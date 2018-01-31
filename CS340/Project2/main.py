from BSTree import Tree
from BSNode import Node

bstTree = Tree()

#String Testing
bstTree.insert(Node("A"))
bstTree.insert(Node("B"))
bstTree.insert(Node("D"))
bstTree.insert(Node("C"))
bstTree.insert(Node("F"))
bstTree.insert(Node("Z"))
bstTree.search("A")
bstTree.search("H")

##Integer Testing
# bstTree.insert(Node(25))
# bstTree.insert(Node(31))
# bstTree.insert(Node(18))
# bstTree.insert(Node(17))
# bstTree.insert(Node(16))
# bstTree.insert(Node(19))
# bstTree.search(45)
# bstTree.search(25)
# bstTree.search(19)


