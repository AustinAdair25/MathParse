import math
from queue import Queue

from nbformat import current_nbformat


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
            # if the current node is right child, remove its parent
            # if not, keep the current parent
            currentParent = list(parentQ.queue)[0]
            if currentParent != None:
                # current node is right node
                if currentParent.rightChild == node:
                    parentQ.get()
                # parent only has left node
                if currentParent.leftChild and not currentParent.rightChild:
                    parentQ.get()

            else:
                parentQ.get()
            # if the node is a leaf, no need to add it to parentQ
            if node.leftChild or node.rightChild:
                parentQ.put(node)

            if not currentParent:
                print(' '*(node.space - currentIndex) + node.value,  end='')
                currentIndex += node.space - currentIndex + 1
            else:
                # current parent has 2 children
                if currentParent.leftChild and currentParent.rightChild:
                    # current node is left child
                    if node == currentParent.leftChild:
                        print(' '*(node.space - currentIndex) +
                              node.value,  end='')
                    # current node is right child
                    if node == currentParent.rightChild:
                        front_space = currentParent.space - currentIndex - 1
                        back_space = node.space - currentParent.space - 2

                        print(' ' + '-'*front_space, end='')
                        print('\'', end='')
                        print('-'*back_space + ' ' + node.value,  end='')

                    # update index
                    currentIndex += node.space - currentIndex + 1

                # current parent has only left child, then current node is the left child
                elif currentParent.leftChild and not currentParent.rightChild:
                    print(' '*(node.space - currentIndex) + node.value,  end='')
                    currentIndex += node.space - currentIndex + 1

                    front_space = currentParent.space - currentIndex - 1
                    print(' ' + '-'*front_space, end='')
                    print('\'', end='')
                    currentIndex += front_space + 2

                # current parent has only right child, then current node is the left child
                elif not currentParent.leftChild and currentParent.rightChild:
                    front_space = currentParent.space - currentIndex - 1
                    back_space = node.space - currentParent.space - 2

                    print(' ' + ' '*front_space, end='')
                    print('\'', end='')
                    print('-'*back_space + ' ' + node.value,  end='')

                    currentIndex += node.space - currentIndex + 1

            if node.leftChild != None:
                queue.put(node.leftChild)
            if node.rightChild != None:
                queue.put(node.rightChild)
        print()

    def findSpaceAndDepth(self, space, node, depth):
        if node == None:
            return space, space

        node.depth = depth
        # go to left subtree
        leftIndex, leftMax = self.findSpaceAndDepth(
            space, node.leftChild, depth + 1)
        # go to right subtree
        rightIndex, rightMax = self.findSpaceAndDepth(
            leftMax + 4, node.rightChild, depth + 1)
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
