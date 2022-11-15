import re


class Tokenizer:
    def __init__(self, string):
        self.tokenList = []
        regex = r'([a-zA-Z][a-zA-Z0-9]*)|[0-9]+(\.[0-9]*)?|\S'
        for mo in re.finditer(regex, string):
            token = mo.group()

    def getTokenList(self):
        return self.tokenList


class Token:
    def __init__(self, value, type):
        self.value = value
        self.type = type
