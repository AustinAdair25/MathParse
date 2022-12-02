from tokenizer import Tokenizer
from parser import Parser

print("CS152 Mathematical Expression Parser")
while True:
    string = input('Enter a mathematical expression (type \':q\' to quit): ')
    if string.strip() == ':q':
        break
    tokens = Tokenizer(string.strip())
    try:
        parser = Parser(tokens.get_token_list())
        parser.parse()
        print("\nThe expression is successfully parsed!\n")
        while True:
            print('1. View the parse tree')
            print('2. Substitute values')
            print('3. Parse a different expression or Go back)')
            choice = input("Entern a choice: ")
            print()
            if choice == '1':
                parser.print()
            elif choice == '2':
                try:
                    result = parser.substitute_values()
                except Exception as ex:
                    print(ex)
                    print()
                    continue
                print('The result: ' + str(result))
            elif choice == '3':
                break
            else:
                print("Invalue choice!")
            print()

    except Exception as ex:
        print(ex)
