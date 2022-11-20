from tokenizer import Tokenizer
from parser import Parser
from binaryTree import TreeNode, BinaryTree
# string = "a^a^a"
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

bTree = BinaryTree(tree)

bTree.findSpace(0, tree)
bTree.root.printTree()