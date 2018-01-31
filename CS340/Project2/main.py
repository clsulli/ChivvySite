from BSTree import Tree
from BSNode import Node

#Save Input File to Array
def fileToArray(file):
    fObj = open(file, "r")
    tempArr = []
    for line in fObj:
        tempArr.append(line.strip("\n"))

    return tempArr

#SelSort
# #Select the Sort Method
# def selectSort():
#     print("Select Sorting Algorithm:")
#     print("     (a) Insertion Sort")
#     print("     (b) Merge Sort")
#     print("     (c) Heap Sort")
#
#     choice = input(">> ")
#
#     if choice == "a" or choice == "A":
#         return 1
#     elif choice == "b" or choice == "B":
#         return 2
#     elif choice == "c" or choice == "C":
#         return 3

#Select File Size

def selectSize():
    print("Select Size:")
    print("     (a) 30K")
    print("     (b) 60K")
    print("     (c) 90K")
    print("     (d) 120K")
    print("     (e) 150K")

    choice = input(">> ")

    if choice == "a" or choice == "A":
        return 1
    elif choice == "b" or choice == "B":
        return 2
    elif choice == "c" or choice == "C":
        return 3
    elif choice == "d" or choice == "D":
        return 4
    elif choice == "e" or choice == "E":
        return 5

#Select Permutated or Sorted
def selectPorS():
        print("Select if Initially Sorted or Permutated:")
        print("     (a) Permutated")
        print("     (b) Sorted")

        choice = input(">> ")

        if choice == "a" or choice == "A":
            return 1
        elif choice == "b" or choice == "B":
            return 2

def setCurrFile(type, size):
    # Init Dependencies
    perm30K = "Wordlists/perm30K.txt"
    perm60K = "Wordlists/perm60K.txt"
    perm90K = "Wordlists/perm90K.txt"
    perm120K = "Wordlists/perm120K.txt"
    perm150K = "Wordlists/perm150K.txt"
    sorted30K = "Wordlists/sorted30K.txt"
    sorted60K = "Wordlists/sorted60K.txt"
    sorted90K = "Wordlists/sorted90K.txt"
    sorted120K = "Wordlists/sorted120K.txt"
    sorted150K = "Wordlists/sorted150K.txt"

    # Determine Selected File
    if type == 1 and size == 1:
        currFile = perm30K
    elif type == 1 and size == 2:
        currFile = perm60K
    elif type == 1 and size == 3:
        currFile = perm90K
    elif type == 1 and size == 4:
        currFile = perm120K
    elif type == 1 and size == 5:
        currFile = perm150K
    elif type == 2 and size == 1:
        currFile = sorted30K
    elif type == 2 and size == 2:
        currFile = sorted60K
    elif type == 2 and size == 3:
        currFile = sorted90K
    elif type == 2 and size == 4:
        currFile = sorted120K
    elif type == 2 and size == 5:
        currFile = sorted150K

    return currFile

def buildBST(tree, arr):
    for iter in range(0,len(arr)):
        tree.insert(Node(arr[iter]))

##MAIN##
size = selectSize()
type = selectPorS()
cFile = setCurrFile(type, size)
cFileArr = fileToArray(cFile)

cFileBST = Tree()
buildBST(cFileBST, cFileArr)
cFileBST.search("ORTHOPTERANS")



# #String Testing
# bstTree.insert(Node("A"))
# bstTree.insert(Node("B"))
# bstTree.insert(Node("D"))
# bstTree.insert(Node("C"))
# bstTree.insert(Node("F"))
# bstTree.insert(Node("Z"))
# bstTree.search("A")
# bstTree.search("H")

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




