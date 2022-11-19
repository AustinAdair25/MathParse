from tokenizer import Tokenizer
from parser import Parser

string = "a^a^a"

tokens = Tokenizer(string)

try:
    Parser(tokens.getTokenList()).Parse()
except Exception as ex:
    print(ex)
