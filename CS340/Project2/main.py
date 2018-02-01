from BSTree import Tree
from BSNode import Node
from RBTree import RBTree
from RBNode import RBNode

#Save Input File to Array
def fileToArray(file):
    fObj = open(file, "r")
    tempArr = []
    for line in fObj:
        tempArr.append(line.strip("\n"))

    return tempArr

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

#Set the Current File
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

#Build a Binary Search Tree
def buildBST(tree, arr):
    for iter in range(0,len(arr)):
        tree.insert(Node(arr[iter]))

#Allow User to Search Specific Tree
def searchForWord(tree):
    stopFlag = 0

    while stopFlag != 1:
        print("     Enter word to search for: ")
        lookingFor = input(">> ")
        tree.search(lookingFor)
        print("     Keep Searching? [Y/N]")
        choice = input(">> ")

        if choice == "y" or choice == "Y":
            stopFlag = 0
        elif choice == "n" or choice == "N":
            stopFlag = 1
            print("Exiting...")
        else:
            stopFlag = 1

##MAIN##
size = selectSize()
type = selectPorS()
cFile = setCurrFile(type, size)
cFileArr = fileToArray(cFile)

cFileBST = Tree()


buildBST(cFileBST, cFileArr)
searchForWord(cFileBST)




