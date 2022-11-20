import math
from queue import Queue

class BinaryTree:

    def __init__(self, root):
        self.root = root

    def printTree(self):
        #BFS
        queue = Queue()
        queue.put(self.root)
        while not queue.empty():
            node = queue



    def findSpace(self, space, node):
        if node == None:   # space: 8
            return space, space
        #go to left subtree
        leftIndex, leftMax = self.findSpace(space, node.leftChild) # 2, 4
        #go to right subtree
        rightIndex, rightMax = self.findSpace(leftMax + 4, node.rightChild) # 10, 12
        #visit current node

        node.space = math.floor((leftIndex + rightIndex)/2)
        return node.space, rightMax




class TreeNode:

    def __init__(self, value):
        self.value = value
        self.rightChild = None
        self.leftChild = None
        self.space = 0

#    def printTree(self):
        #BFS
        # if self == None:
        #     return
        # if self.leftChild != None:
        #     self.leftChild.printTree()
        # if self.rightChild != None:
        #     self.rightChild.printTree()
        #
        # print(self.value, self.space)





