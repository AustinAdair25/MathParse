from logging import raiseExceptions

FUNCTION_NAME = ['sqrt', 'exp', 'log', 'sin', 'cos',
                 'tan', 'arcsin', 'arcsos', 'arctan', 'abs']


class Parser:
    def __init__(self, tokens):
        self.tokens = tokens
        self.currentTokenIndex = 0
        print("parser")

    def Parse(self):
        self.ParseAddition()
        if self.currentTokenIndex < len(self.tokens):
            raise Exception("Invalid Token")

    # expr -> multiplication { ( + | - ) multiplication }
    def ParseAddition(self):
        self.ParseMultiplication()
        operator = self.getCurrentToken()
        while operator and (operator.value == '+' or operator.value == '-'):
            self.next()
            self.ParseMultiplication()
            operator = self.getCurrentToken()

    # multiplication -> power { ( * | / ) power }
    def ParseMultiplication(self):
        self.ParsePower()
        operator = self.getCurrentToken()
        while operator and (operator.value == '*' or operator.value == '/'):
            self.next()
            self.ParsePower()
            operator = self.getCurrentToken()

    # power -> unary { ^ unary }
    def ParsePower(self):
        self.ParseUnary()
        operator = self.getCurrentToken()
        while operator and (operator.value == '^'):
            self.next()
            self.ParseUnary()
            operator = self.getCurrentToken()

    # unary -> { - } token
    def ParseUnary(self):
        operator = self.getCurrentToken()
        if not operator:
            raise Exception(
                "No token found, expect an identifier or unary operation")
        while operator and operator.value == '-':
            self.next()
            operator = self.getCurrentToken()
        self.ParseToken()

    # token ->  function | number
    def ParseToken(self):
        token = self.getCurrentToken()
        if token.type == 'number':
            print(token.value)
            self.next()
        else:
            self.ParseFunction()

    # function -> identifier ["(" expr ")"] | "(" expr ")"
    def ParseFunction(self):
        token = self.getCurrentToken()
        self.next()
        if token.type == "identifier":
            op = self.getCurrentToken()
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
