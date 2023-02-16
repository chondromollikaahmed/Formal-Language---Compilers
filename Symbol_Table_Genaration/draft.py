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
current_scope = "global"

for i, token in enumerate(tokens):
    if token == "int" or token == "float" or token == "double" or token == "char":
        data_type = token
        name = tokens[i+1][1] if type(tokens[i+1]) == tuple else tokens[i+1]
        value = None
        if tokens[i+2] == "=":
            value = tokens[i+3]
        symbol_table.append({"Name": name, "Id": len(symbol_table)+1, "Type": "var", "Data Type": data_type, "Scope": current_scope, "Value": value})
    elif token == "void":
        data_type = token
        name = tokens[i+1][1] if type(tokens[i+1]) == tuple else tokens[i+1]
        symbol_table.append({"Name": name, "Id": len(symbol_table)+1, "Type": "func", "Data Type": data_type, "Scope": current_scope, "Value": None})
        current_scope = name
    elif token == "{":
        current_scope = name
    elif token == "}":
        current_scope = "global"



print(symbol_table)