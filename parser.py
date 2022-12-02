import math
from binaryTree import BinaryTree, TreeNode

FUNCTION_NAME = ['sqrt', 'exp', 'log', 'sin', 'cos',
                 'tan', 'arcsin', 'arcsos', 'arctan', 'abs']


class Parser:
    def __init__(self, tokens):
        self.tokens = tokens
        self.currentTokenIndex = 0
        self.parseTree = None

    def parse(self):
        self.parseTree = BinaryTree(self.parse_addition())
        if self.currentTokenIndex < len(self.tokens):
            raise Exception("Invalid Token")

    def print(self):
        self.parseTree.find_space_and_depth(0, self.parseTree.root, 0)
        self.parseTree.print_tree()

    def substitute_values(self):
        return self.calculate(self.parseTree.root, dict())

    # expr -> multiplication { ( + | - ) multiplication }
    def parse_addition(self):
        currentNode = None
        left = self.parse_multiplication()

        operator = self.get_current_token()
        while operator and (operator.value == '+' or operator.value == '-'):
            self.next()
            right = self.parse_multiplication()

            node = TreeNode(operator)
            node.leftChild = left if currentNode == None else currentNode
            node.rightChild = right
            currentNode = node

            operator = self.get_current_token()

        return left if currentNode == None else currentNode

    # multiplication -> power { ( * | / ) power }
    def parse_multiplication(self):
        current_node = None
        left = self.parse_power()

        operator = self.get_current_token()
        while operator and (operator.value == '*' or operator.value == '/'):
            self.next()
            right = self.parse_power()

            node = TreeNode(operator)
            node.leftChild = left if current_node is None else current_node
            node.rightChild = right
            current_node = node

            operator = self.get_current_token()

        return left if current_node is None else current_node

    # power -> unary { ^ unary }
    def parse_power(self):
        current_node = None
        left = self.parse_unary()

        operator = self.get_current_token()
        while operator and (operator.value == '^'):
            self.next()
            right = self.parse_unary()

            node = TreeNode(operator)
            node.leftChild = left if current_node is None else current_node
            node.rightChild = right
            current_node = node

            operator = self.get_current_token()

        return left if current_node is None else current_node

    # unary -> { - } token
    def parse_unary(self):
        current_node = None
        last_node = None
        operator = self.get_current_token()
        if not operator:
            raise Exception(
                "No token found, expect an identifier or unary operation")
        while operator and operator.value == '-':
            self.next()

            node = TreeNode(operator)

            if current_node:
                node.rightChild = current_node
                current_node = node
            else:
                current_node = node
                last_node = node

            operator = self.get_current_token()
        right = self.parse_token()

        if last_node:
            last_node.rightChild = right
            return current_node
        else:
            return right

    # token ->  function | number
    def parse_token(self):
        token = self.get_current_token()
        if token.type == 'number':
            # print(token.value)
            self.next()
            # create node
            node = TreeNode(token)
            return node
        else:
            return self.parse_function()

    # function -> identifier ["(" expr ")"] | "(" expr ")"
    def parse_function(self):
        token = self.get_current_token()
        self.next()
        if token.type == "identifier":
            node = TreeNode(token)

            op = self.get_current_token()
            if op and op.value == '(':
                if token.value not in FUNCTION_NAME:
                    raise Exception('Invalid function name ' +
                                    '\'' + token.value + '\'')
                self.next()
                result = self.parse_addition()
                # wait for the ')'
                self.is_closed_parenthesis()
                self.next()

                node.leftChild = result
            return node

        elif token.value == '(':
            result = self.parse_addition()
            # wait for the ')'
            self.is_closed_parenthesis()
            self.next()
            return result
        else:
            raise Exception("Can not parse token " + "\'" + token.value + "\'")

    def get_current_token(self):
        index = self.currentTokenIndex
        if index < len(self.tokens):
            return self.tokens[index]
        return None

    def next(self):
        self.currentTokenIndex += 1

    def is_closed_parenthesis(self):
        token = self.get_current_token()
        if not token or token.value != ')':
            raise Exception("Expected ')'")

    def calculate(self, node, hash_map=dict()):
        if node is None:
            return 0

        if node.token.type == "identifier" and node.token.value not in FUNCTION_NAME:
            if not hash_map.get(node.token.value):
                var = input("Please enter a value for " +
                            node.token.value + ": ")
                hash_map[node.token.value] = float(var)
                return float(var)
            else:
                return hash_map[node.token.value]
        elif node.token.type == "number":
            return float(node.token.value)
        elif node.token.type == "operator" or node.token.value in FUNCTION_NAME:
            leftOperant = self.calculate(node.leftChild, hash_map)
            rightOperant = self.calculate(node.rightChild, hash_map)
            #print(leftOperant, righ)
            return self.doMath(node.token.value, leftOperant, rightOperant)

    def doMath(self, operator, left, right):
        if operator == '+':
            return left + right
        elif operator == '-':
            return left - right
        elif operator == '*':
            return left * right
        elif operator == '/':
            return left / right
        elif operator == '^':
            return math.pow(left, right)
        elif operator == 'sqrt':
            return math.sqrt(left + right)
        elif operator == 'exp':
            return math.exp(left + right)
        elif operator == 'log':
            return math.log(left + right)
        elif operator == 'sin':
            return math.sin(left + right)
        elif operator == 'cos':
            return math.cos(left + right)
        elif operator == 'tan':
            return math.tan(left + right)
        elif operator == 'abs':
            return abs(left + right)
        elif operator == 'arcsin':
            return math.asin(left + right)
        elif operator == 'arcsos':
            return math.acos(left + right)
        elif operator == 'arctan':
            return math.atan(left + right)
        else:
            return 0
