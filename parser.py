from binaryTree import BinaryTree, TreeNode

FUNCTION_NAME = ['sqrt', 'exp', 'log', 'sin', 'cos',
                 'tan', 'arcsin', 'arcsos', 'arctan', 'abs']


class Parser:
    def __init__(self, tokens):
        self.tokens = tokens
        self.currentTokenIndex = 0
        self.parseTree = None

    def Parse(self):
        self.parseTree = BinaryTree(self.ParseAddition())
        if self.currentTokenIndex < len(self.tokens):
            raise Exception("Invalid Token")
        self.parseTree.findSpaceAndDepth(0, self.parseTree.root, 0)
        # self.parseTree.root.printTree()
        self.parseTree.printTree()

    # expr -> multiplication { ( + | - ) multiplication }
    def ParseAddition(self):
        currentNode = None
        left = self.ParseMultiplication()

        operator = self.getCurrentToken()
        while operator and (operator.value == '+' or operator.value == '-'):
            self.next()
            right = self.ParseMultiplication()

            node = TreeNode(operator)
            node.leftChild = left if currentNode == None else currentNode
            node.rightChild = right
            currentNode = node

            operator = self.getCurrentToken()

        return left if currentNode == None else currentNode

    # multiplication -> power { ( * | / ) power }
    def ParseMultiplication(self):
        currentNode = None
        left = self.ParsePower()

        operator = self.getCurrentToken()
        while operator and (operator.value == '*' or operator.value == '/'):
            self.next()
            right = self.ParsePower()

            node = TreeNode(operator)
            node.leftChild = left if currentNode == None else currentNode
            node.rightChild = right
            currentNode = node

            operator = self.getCurrentToken()

        return left if currentNode == None else currentNode

    # power -> unary { ^ unary }
    def ParsePower(self):
        currentNode = None
        left = self.ParseUnary()

        operator = self.getCurrentToken()
        while operator and (operator.value == '^'):
            self.next()
            right = self.ParseUnary()

            node = TreeNode(operator)
            node.leftChild = left if currentNode == None else currentNode
            node.rightChild = right
            currentNode = node

            operator = self.getCurrentToken()

        return left if currentNode == None else currentNode

    # unary -> { - } token
    def ParseUnary(self):
        currentNode = None
        operator = self.getCurrentToken()
        if not operator:
            raise Exception(
                "No token found, expect an identifier or unary operation")
        while operator and operator.value == '-':
            self.next()

            node = TreeNode(operator)
            if currentNode:
                currentNode.leftChild = node
            else:
                currentNode = node

            operator = self.getCurrentToken()
        right = self.ParseToken()

        if currentNode:
            currentNode.leftChild = right
            return currentNode
        else:
            return right

    # token ->  function | number
    def ParseToken(self):
        token = self.getCurrentToken()
        if token.type == 'number':
            # print(token.value)
            self.next()
            # create node
            node = TreeNode(token)
            return node
        else:
            return self.ParseFunction()

    # function -> identifier ["(" expr ")"] | "(" expr ")"
    def ParseFunction(self):
        token = self.getCurrentToken()
        self.next()
        if token.type == "identifier":
            node = TreeNode(token)

            op = self.getCurrentToken()
            if op and op.value == '(':
                if token.value not in FUNCTION_NAME:
                    raise Exception('Invalid function name ' +
                                    '\'' + token.value + '\'')
                self.next()
                result = self.ParseAddition()
                # wait for the ')'
                self.isClosedParenthesis()
                self.next()

                node.leftChild = result
            return node

        elif token.value == '(':
            result = self.ParseAddition()
            # wait for the ')'
            self.isClosedParenthesis()
            self.next()
            return result
        else:
            raise Exception("Can not parse token " + "\'" + token.value + "\'")

    def getCurrentToken(self):
        index = self.currentTokenIndex
        if index < len(self.tokens):
            return self.tokens[index]
        return None

    def next(self):
        self.currentTokenIndex += 1

    def isClosedParenthesis(self):
        token = self.getCurrentToken()
        if not token or token.value != ')':
            raise Exception("Expected ')'")
