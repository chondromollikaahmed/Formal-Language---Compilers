import re
from prettytable import PrettyTable
separators =[",",";","'"]
operators = ["+","-","*","/","=","<",">"]
operators2=["+=","-=","*=","/=","<=",">=","++","--"]
parenthesis = ["(",")","{","}","[","]"]
decouple= ["+  =","-  =","*  =","/=","<=",">=","++","--"]
c_keywords= {  "auto", "break", "case", "char", "continue", "do", "default",  "const", 
               "double", "else", "enum", "extern", "for", "if", "goto", "float", 
               "int","long", "register", "return", "signed", "static", "sizeof", "short",
               "struct","switch", "typedef", "union", "void", "while", "volatile","unsigned"}
Ccode = open("source_code.c","r").read()



def remove_block_comments(sourceStr):
  regex=r'/\*.*?\*/'
  matches = re.findall(regex, sourceStr, re.DOTALL)
  for match in matches:
    sourceStr = sourceStr.replace(match, '')
  return sourceStr

Ccode = re.sub(r'\/\/.*\n', '', Ccode) # remove single line comments
Ccode = remove_block_comments(Ccode)
for delim in separators+operators+parenthesis:
    Ccode=Ccode.replace(delim," "+delim+" ")
for decouple in operators2:
    Ccode=Ccode.replace(decouple.replace(decouple,decouple[0]+"  "+decouple[1]),decouple)


tokens = []

for word in Ccode.split():
    if word not in c_keywords and re.match("[_a-zA-Z][_a-zA-Z0-9]*", word):
        tokens.append(("id",word))
    else:
        tokens.append(word)


symbol_table = []
scope_stack = ["global"] # to keep track of the current scope

def add_to_symbol_table(name, identifier_type, data_type, scope, value=None):
    symbol_table.append({
        "Sl. No.": len(symbol_table) + 1,
        "Name": name,
        "Id": identifier_type,
        "Type": data_type,
        "Scope": scope,
        "Value": value
    })

#insert a new entry in the symbol table
def insert(name, identifier_type, data_type, scope, value=None):
    if lookup(name, scope) == -1:
        add_to_symbol_table(name, identifier_type, data_type, scope, value)
    else:
        print("Error: Symbol already exists")


# lookup existing id,scope in symbol table and if found return its index
def lookup(name, scope):
    for i, symbol in enumerate(symbol_table):
        if symbol["Name"] == name and symbol["Scope"] == scope:
            return i
    return -1


# set attributes associate an attribute with a existing entry in the symbol table
def set_attribute(name, scope, attribute, value):
    index = lookup(name, scope)
    if index != -1:
        symbol_table[index][attribute] = value
    else:
        print("Error: Symbol not found")

#free all the memory allocated to the symbol table
def free_symbol_table():
    symbol_table.clear()

#display the symbol table
def display_symbol_table():
    table = PrettyTable()
    table.field_names = ["Sl. No.", "Name", "Id", "Type", "Scope", "Value"]
    for item in symbol_table:
        table.add_row([item['Sl. No.'], item['Name'], item['Id'], item['Type'], item['Scope'], item['Value']])
    print(table)

#exit the program
def exit():
    print("Exiting the program")
    exit(0)


# print("Tokenized Output: ", tokens)
for i, token in enumerate(tokens):
    if token == "int" or token == "float" or token == "double" or token == "char":
        data_type = token
        if tokens[i+1][1] == "main": # special case for main function
            print("On Scope: ", scope_stack[-1])
            add_to_symbol_table("main", "func", data_type, scope_stack[-1])
            scope_stack.append("main")
        else:
            name = tokens[i+1][1]
            if tokens[i+2] == "(": # function case
                print("On Scope: ", scope_stack[-1])
                add_to_symbol_table(name, "func", data_type, scope_stack[-1])
                scope_stack.append(name)
            else: # variable case
                print("On Scope: ", scope_stack[-1])
                add_to_symbol_table(name, "var", data_type, scope_stack[-1])
    elif token == "{": # entering a new scope
        print("apeending :",name)
        # scope_stack.append(name)
    elif token == "}": # exiting a scope
        scope_stack.pop()
    elif token == "=":
        if tokens[i-1][0] == "id":
            name = tokens[i-1][1]
            value = tokens[i+1]
            index = lookup(name, scope_stack[-1])
            if index != -1:
                if not type(tokens[i+1]) == tuple:
                  symbol_table[index]["Value"] = value
            # else:
            #     value = tokens[i+1]
            #     symbol_table[-1]["Value"] = value
    elif token == "int" or token == "float" or token == "double" or token == "char":
        data_type = token
        name = tokens[i+1][1]
        print("On Scope Last Condition: ", scope_stack[-1],name)
        add_to_symbol_table(name, "var", data_type, scope_stack[-1])


table = PrettyTable()
table.field_names = ["Sl. No.", "Name", "Id", "Type", "Scope", "Value"]
for item in symbol_table:
    table.add_row([item['Sl. No.'], item['Name'], item['Id'], item['Type'], item['Scope'], item['Value']])




print(table);



