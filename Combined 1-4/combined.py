
import re
separators =[",",";","'"]
operators = ["+","-","*","/","=","<",">"]
operators2=["+=","-=","*=","/=","<=",">=","++","--"]
parenthesis = ["(",")","{","}","[","]"]
decouple= ["+  =","-  =","*  =","/=","<=",">=","++","--"]
c_keywords= {  "auto", "break", "case", "char", "continue", "do", "default",  "const", 
               "double", "else", "enum", "extern", "for", "if", "goto", "float", 
               "int","long", "register", "return", "signed", "static", "sizeof", "short",
               "struct","switch", "typedef", "union", "void", "while", "volatile","unsigned"}

               

def syntax_error_detection(code):
    # Initialize variables to keep track of parentheses and braces
    open_parentheses = 0
    open_braces = 0
    last_token = ""
    line_number = 1
    
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
            elif token == "}":
                open_braces -= 1
                if open_braces < 0:
                    print(f"Mismatched braces at line {line_number}")
            elif token == "else":
                if last_token != "if":
                    print(f"Unmatched 'else' at line {line_number}")
            elif last_token == token:
                print(f"Duplicate token '{token}' at line {line_number}")
            last_token = token
        line_number += 1
    
    # Check for unbalanced parentheses or braces
    if open_parentheses > 0:
        print(f"Unbalanced parentheses, {open_parentheses} open parentheses remaining")
    elif open_braces > 0:
        print(f"Unbalanced braces, {open_braces} open braces remaining")


def checkInSymbolTable():
    symbol_table = []

    current_scope = "global"

    for token in tokens:
        if token[0] == "id":
            # check if the identifier already exists in the symbol table
            existing_entry = next((entry for entry in symbol_table if entry["Name"] == token[1]), None)

            if existing_entry:
                # update the existing entry with the new scope and value
                existing_entry["Scope"] = current_scope
                existing_entry["Value"] = token[1]
            else:
                # create a new entry for the identifier in the symbol table
                symbol_table.append({"Name": token[1], "Id": len(symbol_table) + 1, "Type": "variable", "Data Type": None, "Scope": current_scope, "Value": token[1]})

        elif token == "int" or token == "double" or token == "float":
            # the next token should be the identifier
            next_token = tokens[tokens.index(token) + 1]
            if next_token[0] == "id":
                # check if the identifier already exists in the symbol table
                existing_entry = next((entry for entry in symbol_table if entry["Name"] == next_token[1]), None)

                if existing_entry:
                    # update the existing entry with the new data type and scope
                    existing_entry["Data Type"] = token
                    existing_entry["Scope"] = current_scope
                else:
                    # create a new entry for the identifier in the symbol table
                    symbol_table.append({"Name": next_token[1], "Id": len(symbol_table) + 1, "Type": "variable", "Data Type": token, "Scope": current_scope, "Value": None})
        elif token == "{":
            current_scope = current_scope + ":" + "block" + str(tokens.index(token))
        elif token == "}":
            current_scope = current_scope.split(":")[0]


        


syntax_error_detection(open("source_code.c","r").read())
