# grammar.py
import ply.yacc as yacc
from lexer import tokens
import random

# Variáveis para armazenar valores
variables = {}

# Precedência e associatividade dos operadores
precedence = (
    ('left', 'PLUS', 'MINUS'),
    ('left', 'TIMES', 'DIVIDE'),
    ('left', 'CONCAT'),
)

# Regras de parsing

def p_program(p):
    'program : statements'
    p[0] = p[1]

def p_statements_multiple(p):
    'statements : statements statement'
    p[0] = p[1] + [p[2]]

def p_statements_single(p):
    'statements : statement'
    p[0] = [p[1]]

def p_statement(p):
    '''statement : assignment_statement
                 | print_statement
                 | read_statement'''
    p[0] = p[1]

def p_assignment_statement(p):
    '''assignment_statement : VARIABLE EQUALS expression SEMICOLON
                            | VARIABLE COLON_EQUALS expression SEMICOLON
                            | VARIABLE EQUALS ENTRADA LPAREN RPAREN SEMICOLON
                            | VARIABLE EQUALS ALEATORIO LPAREN NUMERO RPAREN SEMICOLON'''
    if len(p) == 5 and p[3] == 'ENTRADA':
        p[0] = input("Insira um valor: ")
        variables[p[1]] = p[0]
    elif len(p) == 7 and p[3] == 'ALEATORIO':
        p[0] = random.randint(0, p[6])
        variables[p[1]] = p[0]
    else:
        variables[p[1]] = p[3]
        p[0] = p[3]



def p_print_statement(p):
    '''print_statement : ESCREVER LPAREN expression RPAREN
                       | ESCREVER LPAREN expression RPAREN SEMICOLON'''
    # Realiza a interpolação de strings
    if isinstance(p[3], str):
        output = interpolate_string(p[3])
    else:
        output = p[3]
    print(output)
    p[0] = None

def interpolate_string(s):
    # Substitui as variáveis no formato #{var} pelo valor correspondente
    import re
    pattern = re.compile(r'#\{(\w+)\}')
    return pattern.sub(lambda match: str(variables.get(match.group(1), match.group(0))), s)

def p_read_statement(p):
    '''read_statement : READ LPAREN VARIABLE RPAREN SEMICOLON'''
    input_value = input("Insira um valor para %s: " % p[3])
    variables[p[3]] = int(input_value)
    p[0] = None

def p_expression_binop(p):
    '''expression : expression PLUS expression
                  | expression MINUS expression
                  | expression TIMES expression
                  | expression DIVIDE expression
                  | expression CONCAT expression'''
    if p[2] == '+':
        p[0] = p[1] + p[3]
    elif p[2] == '-':
        p[0] = p[1] - p[3]
    elif p[2] == '*':
        p[0] = p[1] * p[3]
    elif p[2] == '/':
        p[0] = p[1] // p[3]
    elif p[2] == '<>':
        p[0] = str(p[1]) + str(p[3])

def p_expression_group(p):
    'expression : LPAREN expression RPAREN'
    p[0] = p[2]

def p_expression_number(p):
    'expression : NUMERO'
    p[0] = p[1]

def p_expression_string(p):
    'expression : STRING'
    p[0] = p[1]

def p_expression_variable(p):
    'expression : VARIABLE'
    p[0] = variables.get(p[1], 0)

def p_error(p):
    if p:
        print("Erro de sintaxe em '%s'" % p.value)
    else:
        print("Erro de sintaxe no final da entrada")

# Construção do parser
parser = yacc.yacc()

def parse_code(code):
    parser.parse(code)
    return variables

if __name__ == '__main__':
    # Teste de execução do código
    code = '''
    escola := "EST";
    inst := "IPCA";
    ESCREVER ("Olá, #{escola} #{inst}!");
    '''
    result = parse_code(code)
    print("Variáveis finais:", variables)
