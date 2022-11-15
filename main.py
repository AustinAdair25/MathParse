from tokenizer import Tokenizer

string = "cos(x^2+2*pi*theta)/sqrt(a^2+b^2)"

tokens = Tokenizer(string)

print(tokens.getTokenList())
