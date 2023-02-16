import re

# Symbol table to store identifier declarations
symbol_table = {}

def tokenize(code):
    # Define regular expressions for different types of tokens
    token_patterns = {
        'INT': r'\bint\b',
        'FLOAT': r'\bfloat\b',
        'DOUBLE': r'\bdouble\b',
        'IF': r'\bif\b',
        'ELSE': r'\belse\b',
        'RETURN': r'\breturn\b',
        'ID': r'\b[a-zA-Z_][a-zA-Z0-9_]*\b',
        'NUM': r'\b[-+]?[0-9]*\.?[0-9]+([eE][-+]?[0-9]+)?\b',
        'OP': r'[+\-*/=<>!&|%^~]',
        'COMMA': r'[,]',
        'COLON': r'[:]',
        'SEMICOLON': r'[;]',
        'LPAREN': r'[(]',
        'RPAREN': r'[)]',
        'LBRACE': r'[{]',
        'RBRACE': r'[}]'
    }
    # Combine all regular expressions into a single pattern
    pattern = '|'.join('(?P<%s>%s)' % pair for pair in token_patterns.items())
    # Iterate through all matches of the pattern in the code
    for match in re.finditer(pattern, code):
        # Determine which type of token was matched
        for token_type, value in match.groupdict().items():
            if value:
                yield (token_type, value)

def check_syntax_errors(tokens):
    paren_count = 0
    brace_count = 0
    else_flag = False
    symbol_table = {}

    for i, value in enumerate(tokens):
        if value == '(':
            paren_count += 1
        elif value == ')':
            paren_count -= 1
            if paren_count < 0:
                print(f"Error: Unbalanced parentheses at line {i}")
        elif value == '{':
            brace_count += 1
        elif value == '}':
            brace_count -= 1
            if brace_count < 0:
                print(f"Error: Unbalanced braces at line {i}")
        elif value == 'if':
            else_flag = True
        elif value == 'else':
            else_flag = False
        elif value in symbol_table:
            print(f"Error: Duplicate identifier '{value}' at line {i}")
        else:
            symbol_table[value] = i

    if paren_count != 0:
        print(f"Error: Unbalanced parentheses at line {i}")
    if brace_count != 0:
        print(f"Error: Unbalanced braces at line {i}")
    if else_flag:
        print(f"Error: Unmatched 'if' before 'else' at line {i}")

if __name__ == '__main__':
    # Read the source code from file
    with open('source_code.c', 'r') as f:
        code = f.read()
    # Tokenize the source code
    tokens = list(tokenize(code))
    # Check for syntax errors
    check_syntax_errors(tokens)
