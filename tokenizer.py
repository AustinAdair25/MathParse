"""
    Authors: Nhat Le, Austin Adair
    A class that uses Regular Expression to extract all the tokens from the expression
"""

import re


class Tokenizer:
    # constructor
    def __init__(self, string):
        self.tokenList = []
        # regex = r'([a-zA-Z][a-zA-Z0-9]*)|[0-9]+(\.[0-9]*)?|\S'
        regex = r'(?P<identifier>[a-zA-Z][a-zA-Z0-9\.]*)|(?P<number>[0-9]+(\.[0-9]*)?)|(?P<operator>\S)'
        for mo in re.finditer(regex, string):
            token = mo.group()
            self.tokenList.append(Token(token, mo.lastgroup))

    # return the token list
    def get_token_list(self):
        return self.tokenList


class Token:
    # constructor
    def __init__(self, value, type):
        self.value = value
        self.type = type

    # format Token object for print()
    def __str__(self):
        return 'value= ' + self.value + ', type= ' + self.type
