from RBNode import RnBNode
RED = 1
BLACK = 0

def createNILNode():
    node = RnBNode(None)
    node.color = BLACK

    return node

def createNode(key):
    node = RnBNode(key)

    return node
