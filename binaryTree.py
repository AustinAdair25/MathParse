import math
from queue import Queue


class BinaryTree:

    def __init__(self, root):
        self.root = root

    def printTree(self):
        # BFS
        queue = Queue()
        queue.put(self.root)
        currentDepth = 0
        currentIndex = 0
        parentQ = Queue()
        parentQ.put(None)
        while not queue.empty():
            node = queue.get()
            if node.depth != currentDepth:
                currentDepth = node.depth
                currentIndex = 0
                print()
            separator = ' '
            currentParent = parentQ
            if currentParent and currentParent.rightChild == node:
                separator = '-'

            else:
                parentQ.put(node)
            print(separator*(node.space - currentIndex) + node.value,  end='')
            #print(node.space - currentIndex - 1, node.value, currentDepth, currentIndex)
            currentIndex += node.space - currentIndex + 1
            if node.leftChild != None:
                queue.put(node.leftChild)
            if node.rightChild != None:
                queue.put(node.rightChild)
        print()

    def printTree2(self):
        pass

    def findSpaceAndDepth(self, space, node, depth):
        if node == None:   # space: 8
            return space, space

        node.depth = depth
        # go to left subtree
        leftIndex, leftMax = self.findSpaceAndDepth(
            space, node.leftChild, depth + 1)  # 2, 4
        # go to right subtree
        rightIndex, rightMax = self.findSpaceAndDepth(
            leftMax + 4, node.rightChild, depth + 1)  # 10, 12
        # visit current node

        node.space = math.floor((leftIndex + rightIndex)/2)
        return node.space, rightMax


class TreeNode:

    def __init__(self, value):
        self.value = value
        self.rightChild = None
        self.leftChild = None
        self.space = None
        self.depth = None

    def printTree(self):
        if self == None:
            return
        if self.leftChild != None:
            self.leftChild.printTree()
        if self.rightChild != None:
            self.rightChild.printTree()

        print(self.value, self.space, self.depth)
