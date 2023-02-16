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

def generateTokens(stringToken):
    for word in stringToken.split():
        if word not in c_keywords and re.match("[_a-zA-Z][_a-zA-Z0-9]*", word):
            tokens.append(("id",word))
        else:
            tokens.append(word)
    return tokens


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
    # else:
    #     print("Error: Symbol already exists")



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



#generic genrate symbol table function
def generic_symbol_table(tokens):
    for i, token in enumerate(tokens):
        if token == "int" or token == "float" or token == "double" or token == "char":
            data_type = token
            if tokens[i+1][1] == "main": # special case for main function
                insert("main", "func", data_type, scope_stack[-1])
                scope_stack.append("main")
            else:
                name = tokens[i+1][1]
                if tokens[i+2] == "(": # function case

                    insert(name, "func", data_type, scope_stack[-1])
                    scope_stack.append(name)
                else: # variable case
                    insert(name, "var", data_type, scope_stack[-1])
        elif token == "{": # entering a new scope
            continue
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
              
def generate_symbol_table():
    for i, token in enumerate(tokens):
        if token == "int" or token == "float" or token == "double" or token == "char":
            data_type = token
            if tokens[i+1][1] == "main": # special case for main function
                insert("main", "func", data_type, scope_stack[-1])
                scope_stack.append("main")
            else:
                name = tokens[i+1][1]
                if tokens[i+2] == "(": # function case

                    insert(name, "func", data_type, scope_stack[-1])
                    scope_stack.append(name)
                else: # variable case

                    insert(name, "var", data_type, scope_stack[-1])
        elif token == "{": # entering a new scope
           continue
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


def user_choice():
    choice_msg = [
        "Enter 1 for Insert",
        "Enter 2 for Set Attribute",
        "Enter 3 for Free",
        "Enter 4 for LookUp",
        "Enter 5 for Display",
        "Enter 6 for Exit",
    ]

    while True:
        for msg in choice_msg:
            print(msg)

        _user_choice = input('\n Enter your choice from the list: ')

        if _user_choice == '1':
            user_data = input('\n Please enter comma separated data you want to add: ')
            generic_symbol_table(generateTokens(user_data))

            if len(symbol_table) == 0:
                print("Symbol table is empty. Please insert data first! \n")
                continue

        elif _user_choice == '2':
            #name , scope , attribute , value
            user_data = input('\n Please enter name:')
            user_data1 = input('\n Please enter scope:')
            user_data2 = input('\n Please enter attribute:')
            user_data3 = input('\n Please enter value:')
            set_attribute(user_data,user_data1,user_data2,user_data3)
            

        elif _user_choice == '3':
            free_symbol_table()
            print("Symbol table is empty now. \n")


            

        elif _user_choice == '4':
            #name , scope
            user_data = input('\n Please enter name:')
            user_data1 = input('\n Please enter scope:')
            x=lookup(user_data,user_data1)
            if x==-1:
                print("Not Found")
            else:
                #print index with name and scope
                print("Found at index: ",x)
                

            

        elif _user_choice == '5':
            display_symbol_table()

        elif _user_choice == '6':
            break
        else:
            print("You entered a wrong choice. Please try again \n")




generate_symbol_table()

# print(symbol_table)
user_choice()
