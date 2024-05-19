import ply.lex as lex
import ply.yacc as yacc

# Lista de tokens
tokens = [
    'PRINT',         # print
    'READ',          # read
    'NUMERO',        # números
    'STRING',        # strings
    'VARIABLE',      # variáveis
    'LPAREN',        # (
    'RPAREN',        # )
    'PLUS',          # +
    'MINUS',         # -
    'TIMES',         # *
    'DIVIDE',        # /
    'SEMICOLON',     # ;
    'ASSIGNMENT',    # :=
    'CONCAT',        # <>
]

# Ignorar espaços em branco e tabulações
t_ignore = ' \t\n'

# Definições de expressões regulares para tokens simples
t_LPAREN = r'\('
t_RPAREN = r'\)'
t_PLUS = r'\+'
t_MINUS = r'-'
t_TIMES = r'\*'
t_DIVIDE = r'/'
t_SEMICOLON = r';'
t_ASSIGNMENT = r':='
t_CONCAT = r'<>'

def t_PRINT(t):
    r'PRINT'
    return t

def t_READ(t):
    r'READ'
    return t

def t_NUMERO(t):
    r'\d+'
    t.value = int(t.value)
    return t

def t_STRING(t):
    r'"([^\\"]|\\.)*"'
    t.value = t.value[1:-1]  # Remover as aspas
    return t

# Regra de expressão regular para variáveis
def t_VARIABLE(t):
    r'[a-z_][a-zA-Z0-9_]*[\?\!]?'
    return t

# Regra de tratamento de erro
def t_error(t):
    print("Caractere incorreto: '%s'" % t.value[0])
    t.lexer.skip(1)

# Construção do lexer
lexer = lex.lex()

# Função para imprimir tokens
def print_tokens(code):
    lexer.input(code)
    for token in lexer:
        print(token)

# Teste para imprimir tokens
code = '''
tmp_01 := 2*3+4 ;
a1_ := 12345 - (5191 * 15) ;
idade_valida? := 1;
mult_3! := a1_ * 3 ;
'''
print("Tokens:")
print_tokens(code)
print("\nParsing and Execution:\n")

# Regras de parsing
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

# Regra para statement
def p_statement(p):
    '''statement : assignment_statement
                 | print_statement
                 | read_statement'''
    p[0] = p[1]

# Regra para atribuição
def p_assignment_statement(p):
    '''assignment_statement : VARIABLE ASSIGNMENT expression SEMICOLON'''
    variables[p[1]] = p[3]
    p[0] = p[3]

# Regra para print
def p_print_statement(p):
    '''print_statement : PRINT LPAREN expression RPAREN SEMICOLON'''
    print(p[3])
    p[0] = None

# Regra para leitura
def p_read_statement(p):
    '''read_statement : READ LPAREN VARIABLE RPAREN SEMICOLON'''
    input_value = input("Insira um valor para %s: " % p[3])
    variables[p[3]] = int(input_value)
    p[0] = None

# Regra para expressão
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

# Regra para tratamento de erro
def p_error(p):
    print("Erro de sintaxe.")

# Construção do parser
parser = yacc.yacc()

# Função para execução do código
def run(code):
    parser.parse(code)
    return variables

# Teste de execução do código
code = '''
tmp_01 := 2*3+4 ;
a1_ := 12345 - (5191 * 15) ;
idade_valida? := 1;
mult_3! := a1_ * 3 ;
PRINT(mult_3!);
'''
result = run(code)
print("Variáveis finais:", variables)

# Função principal para execução com arquivo de entrada
def main():
    import sys
    if len(sys.argv) > 1:
        with open(sys.argv[1], 'r') as file:
            data = file.read()
        run(data)
        print("Variáveis finais:", variables)
    else:
        data = ""
        print("Insira os comandos (terminar com CTRL+D):")
        while True:
            try:
                line = input()
            except EOFError:
                break
            data += line + '\n'
        run(data)
        print("Variáveis finais:", variables)

if __name__ == '__main__':
    main()
