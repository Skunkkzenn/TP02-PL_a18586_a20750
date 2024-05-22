#grammar.py
import ply.yacc as yacc
from lexer import tokens

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
                             | VARIABLE LPAREN expression RPAREN SEMICOLON
                             | VARIABLE COLON EQUALS expression SEMICOLON
                             | ESCREVER LPAREN expression RPAREN SEMICOLON'''
    if len(p) == 5 or len(p) == 6:
        variables[p[1]] = p[3]
    p[0] = p[3]

def p_print_statement(p):
    '''print_statement : ESCREVER LPAREN expression RPAREN'''
    print(p[3])
    p[0] = None

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
    print("Erro de sintaxe.")

# Construção do parser
parser = yacc.yacc()

def parse_code(code):
    parser.parse(code)
    return variables

if __name__ == '__main__':
    # Teste de execução do código
    code = '''
    tmp_01 := 2*3+4 ;
    a1_ := 12345 - (5191 * 15) ;
    idade_valida? := 1;
    mult_3! := a1_ * 3 ;
    PRINT(mult_3!);
    '''
    result = parse_code(code)
    print("Variáveis finais:", variables)