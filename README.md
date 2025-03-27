# Mathematical Expression Parser

Welcome to the Mathematical Expression Parser repository! This project validates and evaluates mathematical expressions based on a custom grammar. It supports functions, operators, and parsing to an abstract syntax tree (AST) for visualization.

## 🚀 About This Project
This parser evaluates mathematical expressions, constructs an abstract syntax tree, and substitutes values into variables for evaluation. It's built in Python and supports various functions such as square roots, exponents, and trigonometric operations.

## 🎨 Features
- **Expression Validation**: Validates mathematical expressions based on predefined grammar rules.
- **Abstract Syntax Tree**: Visualizes the structure of the parsed expression.
- **Expression Evaluation**: Computes results by substituting values for variables.
- **Custom Functions**: Supports functions like `sqrt()`, `log()`, `exp()`, and trigonometric functions.

## 🛠️ Technologies Used
- **Python 3.x** - Programming language
- **math library** - For mathematical functions
- **queue library** - For managing operator precedence during parsing

## 📂 Files Overview
- **binaryTree.py**: Defines the `BinaryTree` and `TreeNode` classes for constructing and visualizing the parse tree.
- **grammar.txt**: Contains the grammar rules used by the parser.
- **main.py**: Entry point that handles user input, parsing, and interaction.

## 🧑‍💻 Grammar

This parser follows the following grammar rules for mathematical expressions:

expr -> multiplication { ( + | - ) multiplication } multiplication -> power { ( * | / ) power } | ml -> power power -> unary { ^ unary } unary -> [ - ] token token -> function | number function -> identifier ["(" expr ")"] | "(" expr ")" number -> [0..9]+(.[0..9]+)? identifier -> [a-zA-Z][a-zA-Z0-9]*


### Operators:
- `+`, `-`: Addition and Subtraction
- `*`, `/`: Multiplication and Division
- `^`: Exponentiation
- `-`: Unary negation

### Functions:
- `sqrt()`, `exp()`, `log()`, `sin()`, `cos()`, `tan()`, `arcsin()`, `arccos()`, `arctan()`, `abs()`

## 🛠️ Installation & Setup
To run this project locally, follow these steps:

1. **Clone the repository:**
   ```sh
   git clone https://github.com/yourusername/mathematical-expression-parser.git

2. **Navigate to the project directory:**
   ```sh
   cd mathematical-expression-parser
(Optional) Set up a virtual environment:
python3 -m venv venv
source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
Install dependencies (if any):
pip install -r requirements.txt
Run the program:
python main.py
🎮 Example Usage

Enter a mathematical expression, e.g., 3 + 5 * (2 - 8).
The program will parse and validate the expression.
Choose an option to view the parse tree or substitute values into variables.
📩 Contact Me

Feel free to reach out for questions or collaboration opportunities:

Email: [Your Email Here]
LinkedIn: [Your LinkedIn Here]
💡 If you like this project, consider giving it a star on GitHub! ⭐
