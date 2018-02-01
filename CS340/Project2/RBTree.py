from RBNode import RBNode

class RBTree():

    RED = 1
    BLACK = 0

    NIL = RBNode(None, BLACK)

    def __init__(self, root=None):
        self.root = root

    def insertFixup(self, iNode):
        RED = 1
        BLACK = 0

        while iNode.parent.color == RED:
            if iNode.parent == iNode.parent.parent.lChild:
                tNode = iNode.parent.parent.rChild
                if tNode.color == RED:
                    iNode.parent.color = BLACK
                    tNode.color = BLACK
                    iNode.parent.parent.color = RED
                    iNode = iNode.parent.parent
                else:
                    if iNode == iNode.parent.rChild:
                        iNode = iNode.parent
                        self.leftRotate(iNode)
                    iNode.parent.color = BLACK
                    iNode.parent.parent.color = RED
                    self.rightRotate(iNode.parent.parent)
            else:
                tNode = iNode.parent.parent.lChild
                if tNode.color == RED:
                    iNode.parent.color = BLACK
                    tNode.color = BLACK
                    iNode.parent.parent.color = RED
                    iNode = iNode.parent.parent
                else:
                    if iNode == iNode.parent.lChild:
                        iNode = iNode.parent
                        self.rightRotate(iNode)
                    iNode.parent.color = BLACK
                    iNode.parent.parent.color = RED
                    self.leftRotate(iNode.parent.parent)

        self.root.color = BLACK

    def insert(self, iNode):

        BLACK = 0
        RED = 1

        #DESCRIPTION
            #If BST is empty
                # iNode parent is type None because iNode is root.  Then sets tree.root to be iNode
            #If BST is populated
                # runs down the tree until reaching None, sets the parent of insert Node to be 1 level
                # higher, then checks if iNode is less than or greater than parent and assigns it lChild or rChild

        cNode = self.root#x
        tNode = self.NIL #y

        while cNode != self.NIL:

            tNode = cNode

            if iNode.key < cNode.key:
                cNode = cNode.lChild
            else:
                cNode = cNode.rChild

        iNode.parent = tNode

        if tNode == self.NIL:
            self.root = iNode
        elif iNode.key < tNode.key:
            tNode.lChild = iNode
        else:
            tNode.rChild = iNode

        iNode.rChild = self.NIL
        iNode.lChild = self.NIL
        iNode.color = RED

        self.insertFixup(iNode)

        # if self.root == iNode:
        #     print("Added Child " + str(iNode.key) + " at Root")
        # else:
        #     print("Added Child " + str(iNode.key) + ": Parent" + str(iNode.parent.key))

        return iNode

    def search(self, lookingFor):
        cNode = self.root

        while cNode != None and lookingFor != cNode.key:
            if lookingFor < cNode.key:
                cNode = cNode.lChild
            elif lookingFor > cNode.key:
                cNode = cNode.rChild

        if cNode == None:
            result = str(lookingFor) + " was not found in the Tree."
        elif cNode.key == lookingFor:
            result = str(lookingFor) + " was found in the Tree."
        else:
            result = "Error"

        return print(result)

    def leftRotate(self, cNode):
        #tNode = y
        #iNode = z
        #cNode = x

        tNode = cNode.rChild
        cNode.rChild = tNode.lChild
        if tNode.lChild != self.NIL:
            tNode.lChild.parent = cNode
        tNode.parent = cNode.parent
        if cNode.parent == self.NIL:
            self.root = tNode
        else:
            if cNode == cNode.parent.lChild:
                cNode.parent.lChild = tNode
            else:
                cNode.parent.rChild = tNode

        tNode.lChild = cNode
        cNode.parent = tNode

    def rightRotate(self, cNode):
        #tNode = y
        #iNode = z
        #cNode = x

        tNode = cNode.lChild
        cNode.lChild = tNode.rChild
        if tNode.rChild == self.NIL:
            tNode.rChild.parent = cNode
        tNode.parent = cNode.parent
        if cNode.parent == self.NIL:
            self.root = tNode
        else:
            if cNode == cNode.parent.rChild:
                cNode.parent.rChild = tNode
            else:
                cNode.parent.lChild = tNode

        tNode.rChild = cNode
        cNode.parent = tNode
















