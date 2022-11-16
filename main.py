from tokenizer import Tokenizer
from parser import Parser

string = "cos(x^2+2*pi*theta)/sqrt(a^2+b^2)"

tokens = Tokenizer(string)

try:
    Parser(tokens.getTokenList()).Parse()
except Exception as ex:
    print(ex)
