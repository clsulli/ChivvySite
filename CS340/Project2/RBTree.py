import Properties

class RnBTree():

    def __init__(self, root=None, NIL=None):
        self.root = Properties.createNode(None)
        self.NIL = Properties.createNILNode()
        self.root = self.NIL

    def insertFixup(self, iNode):

        while iNode.parent.color == Properties.RED:
            if iNode.parent == iNode.parent.parent.lChild:
                tNode = iNode.parent.parent.rChild
                if tNode.color == Properties.RED:
                    iNode.parent.color = Properties.BLACK
                    tNode.color = Properties.BLACK
                    iNode.parent.parent.color = Properties.RED
                    iNode = iNode.parent.parent
                else:
                    if iNode == iNode.parent.rChild:
                        iNode = iNode.parent
                        self.leftRotate(iNode)
                    iNode.parent.color = Properties.BLACK
                    iNode.parent.parent.color = Properties.RED
                    self.rightRotate(iNode.parent.parent)
            else:
                tNode = iNode.parent.parent.lChild
                if tNode.color == Properties.RED:
                    iNode.parent.color = Properties.BLACK
                    tNode.color = Properties.BLACK
                    iNode.parent.parent.color = Properties.RED
                    iNode = iNode.parent.parent
                else:
                    if iNode == iNode.parent.lChild:
                        iNode = iNode.parent
                        self.rightRotate(iNode)
                    iNode.parent.color = Properties.BLACK
                    iNode.parent.parent.color = Properties.RED
                    self.leftRotate(iNode.parent.parent)

        self.root.color = Properties.BLACK

    def insert(self, iNode):

        #DESCRIPTION
            #If BST is empty
                # iNode parent is type None because iNode is root.  Then sets tree.root to be iNode
            #If BST is populated
                # runs down the tree until reaching None, sets the parent of insert Node to be 1 level
                # higher, then checks if iNode is less than or greater than parent and assigns it lChild or rChild

        tNode = self.NIL #y
        cNode = self.root#x

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
        iNode.color = Properties.RED

        self.insertFixup(iNode)

        # if self.root == iNode:
        #     print("Added Child " + str(iNode.key) + " at Root")
        # else:
        #     print("Added Child " + str(iNode.key) + ": Parent" + str(iNode.parent.key))

        return iNode

    def search(self, lookingFor):
        cNode = self.root

        while cNode != self.NIL and lookingFor != cNode.key:
            if lookingFor < cNode.key:
                cNode = cNode.lChild
            elif lookingFor > cNode.key:
                cNode = cNode.rChild

        if cNode == self.NIL:
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
        elif cNode == cNode.parent.lChild:
            cNode.parent.lChild = tNode
        else:
            cNode.parent.rChild = tNode

        tNode.lChild = cNode
        cNode.parent = tNode

    def rightRotate(self, tNode):
        #tNode = y
        #iNode = z
        #cNode = x

        cNode = tNode.lChild
        tNode.lChild = cNode.rChild

        if cNode.rChild != self.NIL:
            cNode.rChild.parent = tNode
        cNode.parent = tNode.parent
        if tNode.parent == self.NIL:
            self.root = cNode
        elif tNode == tNode.parent.rChild:
            tNode.parent.rChild = cNode
        else:
            tNode.parent.lChild = cNode
        cNode.rChild = tNode
        tNode.parent = cNode
















