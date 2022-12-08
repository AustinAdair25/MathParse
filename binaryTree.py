"""
    Authors: Nhat Le, Austin Adair
    A class that stores tokens in a way that follows precedence of operators
"""

import math
from queue import Queue


class BinaryTree:
    # constructor
    def __init__(self, root):
        self.root = root

    # print the tree to the console
    def print_tree(self):
        # BFS
        queue = Queue()
        queue.put(self.root)
        current_depth = 0
        current_index = 0
        parent_q = Queue()
        parent_q.put(None)
        while not queue.empty():
            node = queue.get()
            if node.depth != current_depth:
                current_depth = node.depth
                current_index = 0
                print()
            # if the current node is right child, remove its parent
            # if not, keep the current parent
            current_parent = list(parent_q.queue)[0]
            if current_parent is not None:
                # current node is right node
                if current_parent.rightChild == node:
                    parent_q.get()
                # parent only has left node
                if current_parent.leftChild and not current_parent.rightChild:
                    parent_q.get()

            else:
                parent_q.get()
            # if the node is a leaf, no need to add it to parent_q
            if node.leftChild or node.rightChild:
                parent_q.put(node)

            if not current_parent:
                print(' '*(node.space - len(node.token.value) -
                      current_index) + node.token.value,  end='')
                current_index += node.space - current_index
            else:
                # current parent has 2 children
                if current_parent.leftChild and current_parent.rightChild:
                    # current node is left child
                    if node == current_parent.leftChild:
                        print(' '*(node.space - len(node.token.value) -
                              current_index) + node.token.value,  end='')
                    # current node is right child
                    if node == current_parent.rightChild:
                        front_space = current_parent.space - \
                            len(current_parent.token.value) - current_index - 1
                        back_space = node.space - \
                            len(node.token.value) - (current_parent.space -
                                                     len(current_parent.token.value)) - 2

                        print(' ' + '-'*front_space, end='')
                        print('\'', end='')
                        print('-'*back_space + ' ' + node.token.value,  end='')

                    # update index
                    current_index += node.space - current_index

                # current parent has only left child, then current node is the left child
                elif current_parent.leftChild and not current_parent.rightChild:
                    print(' '*(node.space - len(node.token.value) -
                          current_index) + node.token.value,  end='')
                    current_index += node.space - current_index

                    front_space = current_parent.space - \
                        len(current_parent.token.value) - current_index - 1
                    print(' ' + '-'*front_space, end='')
                    print('\'', end='')
                    current_index += front_space + 2

                # current parent has only right child, then current node is the left child
                elif not current_parent.leftChild and current_parent.rightChild:
                    front_space = current_parent.space - \
                        len(current_parent.token.value) - current_index - 1
                    back_space = node.space - \
                        len(node.token.value) - (current_parent.space -
                                                 len(current_parent.token.value)) - 2

                    print(' ' + ' '*front_space, end='')
                    print('\'', end='')
                    print('-'*back_space + ' ' + node.token.value,  end='')

                    current_index += node.space - current_index

            if node.leftChild is not None:
                queue.put(node.leftChild)
            if node.rightChild is not None:
                queue.put(node.rightChild)
        print()

    # determine the space and depth for each tree node
    def find_space_and_depth(self, space, node, depth):
        if node == None:
            return space, space

        node.depth = depth
        # go to left subtree
        leftIndex, leftMax = self.find_space_and_depth(
            space, node.leftChild, depth + 1)
        # go to right subtree
        rightIndex, rightMax = self.find_space_and_depth(
            leftMax + 6, node.rightChild, depth + 1)
        # visit current node

        node.space = math.floor(
            (leftIndex + rightIndex)/2) + len(node.token.value)
        return node.space, rightMax


class TreeNode:
    # constructor
    def __init__(self, token):
        self.token = token
        self.rightChild = None
        self.leftChild = None
        self.space = None
        self.depth = None
