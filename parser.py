from logging import raiseExceptions

FUNCTION_NAME = ['sqrt', 'exp', 'log', 'sin', 'cos',
                 'tan', 'arcsin', 'arcsos', 'arctan', 'abs']


class Parser:
    def __init__(self, tokens):
        self.tokens = tokens
        self.nextTokenIndex = 0
        print("parser")

    def Parse(self):
        self.ParseAddition()
        if self.nextTokenIndex < len(self.tokens):
            raise Exception("Invalid Token")

    # expr -> multiplication { ( + | - ) multiplication }
    def ParseAddition(self):
        self.ParseMultiplication()
        operator = self.getNextToken()
        while operator and (operator.value == '+' or operator.value == '-'):
            self.next()
            self.ParseMultiplication()
            operator = self.getNextToken()

    # multiplication -> power { ( * | / ) power }
    def ParseMultiplication(self):
        self.ParsePower()
        operator = self.getNextToken()
        while operator and (operator.value == '*' or operator.value == '/'):
            self.next()
            self.ParsePower()
            operator = self.getNextToken()

    # power -> unary { ^ unary }
    def ParsePower(self):
        self.ParseUnary()
        operator = self.getNextToken()
        while operator and (operator.value == '^'):
            self.next()
            self.ParseUnary()
            operator = self.getNextToken()

    # unary -> { - } token
    def ParseUnary(self):
        operator = self.getNextToken()
        if not operator:
            raise Exception(
                "No token found, expect an identifier or unary operation")
        while operator and operator.value == '-':
            self.next()
            operator = self.getNextToken()
        self.ParseToken()

    # token ->  function | number
    def ParseToken(self):
        token = self.getNextToken()
        if token.type == 'number':
            print(token.value)
            self.next()
        else:
            self.ParseFunction()

    # function -> identifier ["(" expr ")"] | "(" expr ")"
    def ParseFunction(self):
        token = self.getNextToken()
        self.next()
        if token.type == "identifier":
            op = self.getNextToken()
            if op and op.value == '(':
                if token.value not in FUNCTION_NAME:
                    raise Exception('Invalid function name ' +
                                    '\'' + token.value + '\'')
                self.next()
                self.ParseAddition()
                # wait for the ')'
                self.isClosedParenthesis()
                self.next()
            else:
                print(token.value)

        elif token.value == '(':
            self.ParseAddition()
            # wait for the ')'
            self.isClosedParenthesis()
            self.next()
        else:
            raise Exception("Can not parse token " + "\'" + token.value + "\'")

    def getNextToken(self):
        index = self.nextTokenIndex
        if index < len(self.tokens):
            return self.tokens[index]
        return None

    def next(self):
        self.nextTokenIndex += 1

    def isClosedParenthesis(self):
        token = self.getNextToken()
        if not token or token.value != ')':
            raise Exception("Expected ')'")
