import re

def syntax_error_detection(code):
    # Initialize variables to keep track of parentheses and braces
    open_parentheses = 0
    open_braces = 0
    last_token = ""
    line_number = 1
    symbol_table = {}
    current_scope = "global"
    
    # Split the code into lines
    lines = code.split("\n")
    for line in lines:
        # Remove comments
        line = re.sub(r"/\*.*\*/", "", line)
        line = re.sub(r"//.*", "", line)
        # Split the line into tokens
        tokens = re.findall(r"[\w]+|[{}()=;,]", line)
        for token in tokens:
            if token == "(":
                open_parentheses += 1
            elif token == ")":
                open_parentheses -= 1
                if open_parentheses < 0:
                    print(f"Mismatched parentheses at line {line_number}")
            elif token == "{":
                open_braces += 1
                # Check if the token is a function or a block
                if last_token in ["int", "float", "double"]:
                    current_scope = last_token
                else:
                    current_scope += "." + last_token
            elif token == "}":
                open_braces -= 1
                current_scope = current_scope.rsplit(".", 1)[0]
                if open_braces < 0:
                    print(f"Mismatched braces at line {line_number}")
            elif token == "else":
                if last_token != "if":
                    print(f"Unmatched 'else' at line {line_number}")
            elif last_token == token:
                print(f"Duplicate token '{token}' at line {line_number}")
            elif last_token in ["int", "float", "double"] and token not in ["(", ")", "{", "}"]:
                # Check if the identifier already exists in the symbol table
                if token in symbol_table:
                    symbol_table[token]["scope"] = current_scope
                else:
                    symbol_table[token] = {"id": token, "type": last_token, "data_type": "var", "scope": current_scope, "value": None}
            last_token = token
        line_number += 1
    
    # Check for unbalanced parentheses or braces
    if open_parentheses > 0:
        print(f"Unbalanced parentheses, {open_parentheses} open parentheses remaining")
    elif open_braces > 0:
        print(f"Unbalanced braces, {open_braces} open braces remaining")

    return symbol_table


syntax_error_detection(open("source_code.c","r").read())