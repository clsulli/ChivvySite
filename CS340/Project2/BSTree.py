import BSNode

class Tree():

    def __init__(self, root=None):
        self.root = root

    def insert(self, iNode):

        #DESCRIPTION
            #If BST is empty
                # iNode parent is type None because iNode is root.  Then sets tree.root to be iNode
            #If BST is populated
                # runs down the tree until reaching None, sets the parent of insert Node to be 1 level
                # higher, then checks if iNode is less than or greater than parent and assigns it lChild or rChild

        cNode = self.root
        tNode = None

        while cNode != None:

            tNode = cNode

            if iNode.key < cNode.key:
                cNode = cNode.lChild
            else:
                cNode = cNode.rChild

        iNode.parent = tNode

        if tNode == None:
            self.root = iNode
        elif iNode.key < tNode.key:
            tNode.lChild = iNode
        else:
            tNode.rChild = iNode

        if self.root == iNode:
            print("Added Child " + str(iNode.key) + " at Root")
        else:
            print("Added Child " + str(iNode.key) + ": Parent" + str(iNode.parent.key))

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















