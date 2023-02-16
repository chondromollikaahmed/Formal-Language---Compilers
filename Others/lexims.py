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
Ccode = open("input.c","r").read()
for delim in separators+operators+parenthesis:
    Ccode=Ccode.replace(delim," "+delim+" ")
for decouple in operators2:
    Ccode=Ccode.replace(decouple.replace(decouple,decouple[0]+"  "+decouple[1]),decouple)
for word in Ccode.split():
        print(("[ kw "+word+" ]") if word in c_keywords else ("[ id "+word+" ]" if re.match("[_a-zA-Z][_a-zA-Z0-9]*", word) else("[ sep "+word+" ]" if word in separators else ("[ op "+word+" ]" if word in operators+operators2 else ("[ par "+word+" ]" if word in parenthesis else ("[ num "+word+" ]" if re.match("^(?=.)([+-]?([0-9]*)(\.([0-9]+))?)$",word) else ("[ unkn "+word+" ]")))))),end="")
