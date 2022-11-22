from tokenizer import Tokenizer
from parser import Parser
from binaryTree import TreeNode, BinaryTree
# string = "a^a^a" -> a = 2 -> ...
#
# tokens = Tokenizer(string)
#
# try:
#     Parser(tokens.getTokenList()).Parse()
# except Exception as ex:
#     print(ex)
tree = TreeNode('root')
a = TreeNode('a')
b = TreeNode('b')
tree.leftChild = a
tree.rightChild = b
c = TreeNode('c')
d = TreeNode('d')
a.leftChild = c
a.rightChild = d
e = TreeNode('e')
f = TreeNode('f')
b.leftChild = e
b.rightChild = f
g = TreeNode('g')
h = TreeNode('h')
e.leftChild = g
e.rightChild = h

i = TreeNode('i')
g.rightChild = i

x = TreeNode('x')
y = TreeNode('y')
i.leftChild = x
i.rightChild = y

m = TreeNode('m')
n = TreeNode('n')
x.leftChild = m
x.rightChild = n


bTree = BinaryTree(tree)

bTree.findSpaceAndDepth(0, tree, 0)
bTree.printTree()
