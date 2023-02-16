symbol_table = {}
keywords = ['int', 'float', 'double', 'return', 'main', 'void']
operators = ['+', '-', '*', '/', '%', '=', '==', '!=', '<', '>', '<=', '>=', '&&', '||', '!']
separators = [';', '(', ')', '{', '}']


import re

def add_symbol(name, id, type, data_type, scope, value=None):
    symbol_table[name] = {'Id': id, 'Type': type, 'Data Type': data_type, 'Scope': scope, 'Value': value}

def tokenize(code):
    tokens = []
    code = re.sub(r'\/\/.*\n', '', code) # remove single line comments
    code = re.sub(r'/\*.*\*/', '', code) # remove multi-line comments
    for s in re.findall(r'\b\w+\b|[^\w\s]', code): # find all keywords, identifiers, operators and separators
        if s in keywords:
            tokens.append(('KEYWORD', s))
        elif s in operators:
            tokens.append(('OP', s))
        elif s in separators:
            tokens.append(('SEP', s))
        elif re.match(r'^[a-zA-Z_]\w*$', s):
            tokens.append(('ID', s))
        elif re.match(r'^\d+\.\d+$|^\d+$', s):
            tokens.append(('NUM', s))
    return tokens

code = """
float x1 = 3.125;
double f1(int x)
{
double z;
z = 0.01;
return z;
}
int main(void)
{
int n1; double z;
n1=25; z=f1(n1);
}
"""


tokenized_output = tokenize(code)
# print(tokens)




# ...

symbol_table = []
current_scope = 'global'
id_counter = 1

for token in tokenized_output:
    token_type = token[0]
    token_value = token[1]

    if token_type == 'KEYWORD':
        data_type = token_value
    elif token_type == 'ID':
        name = token_value
        if token_value in [t[1] for t in tokenized_output[:tokenized_output.index(token)]] :
            type_ = 'var'
            value = None
        else:
            type_ = 'func'
            value = None
            current_scope = name
    elif token_type == 'NUM':
        value = token_value
    elif token_type == 'SEP' and token_value == '{':
        current_scope = name
    elif token_type == 'SEP' and token_value == '}':
        current_scope = 'global'
    elif token_type == 'OP' and token_value == '=':
        value = tokenized_output[tokenized_output.index(token) + 1][1]
    if token_type == 'ID' or (token_type == 'OP' and token_value == '='):
        symbol_table.append({'name': name, 'id': id_counter, 'type': type_, 'data_type': data_type, 'scope': current_scope, 'value': value})
        id_counter += 1
print(symbol_table)

for i in symbol_table:
    print(i)
