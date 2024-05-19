import ply.lex as lex
import ply.yacc as yacc
import random

# Lista de tokens
tokens = [
    'NUMBER',
    'IDENTIFIER',
    'STRING',
    'PLUS',
    'MINUS',
    'TIMES',
    'DIVIDE',
    'LPAREN',
    'RPAREN',
    'ASSIGN',
    'SEMICOLON',
    'CONCAT'
]

# Regras de expressão regular para tokens simples
t_PLUS = r'\+'
t_MINUS = r'-'
t_TIMES = r'\*'
t_DIVIDE = r'/'
t_LPAREN = r'\('
t_RPAREN = r'\)'
t_ASSIGN = r'='
t_SEMICOLON = r';'
t_CONCAT = r'<>'

# Regras para tokens mais complexos
def t_NUMBER(t):
    r'\d+'
    t.value = int(t.value)
    return t

def t_IDENTIFIER(t):
    r'[a-zA-Z_][a-zA-Z0-9_]*[\?\!]?'
    return t

def t_STRING(t):
    r'"([^\\"]|\\.)*"'
    t.value = t.value[1:-1]  # Remover as aspas
    return t

# Ignorar espaços e tabs
t_ignore = ' \t'

# Definição de comentários
def t_COMMENT(t):
    r'\-\-.*'
    pass  # Ignorar comentários de linha única

def t_MULTILINE_COMMENT(t):
    r'\{\-.*?-\}'
    pass  # Ignorar comentários de múltiplas linhas

# Tratamento de erros
def t_error(t):
    print(f"Caractere ilegal '{t.value[0]}'")
    t.lexer.skip(1)

# Construir o léxico
lexer = lex.lex()

# Precedência dos operadores
precedence = (
    ('left', 'PLUS', 'MINUS'),
    ('left', 'TIMES', 'DIVIDE'),
)

# Dicionário para armazenar as variáveis
variables = {}

# Definição da gramática
def p_program(p):
    'program : statements'
    p[0] = p[1]

def p_statements_multiple(p):
    'statements : statements statement'
    p[0] = p[1] + [p[2]]

def p_statements_single(p):
    'statements : statement'
    p[0] = [p[1]]

def p_statement_assign(p):
    'statement : IDENTIFIER ASSIGN expression SEMICOLON'
    variables[p[1]] = p[3]

def p_statement_write(p):
    'statement : ESCREVER LPAREN expression RPAREN SEMICOLON'
    print(p[3])

def p_statement_input(p):
    'statement : IDENTIFIER ASSIGN ENTRADA LPAREN RPAREN SEMICOLON'
    variables[p[1]] = int(input("Input: "))

def p_statement_random(p):
    'statement : IDENTIFIER ASSIGN ALEATORIO LPAREN NUMBER RPAREN SEMICOLON'
    variables[p[1]] = random.randint(0, p[5])

def p_expression_binop(p):
    '''expression : expression PLUS expression
                  | expression MINUS expression
                  | expression TIMES expression
                  | expression DIVIDE expression'''
    if p[2] == '+':
        p[0] = p[1] + p[3]
    elif p[2] == '-':
        p[0] = p[1] - p[3]
    elif p[2] == '*':
        p[0] = p[1] * p[3]
    elif p[2] == '/':
        p[0] = p[1] // p[3]

def p_expression_group(p):
    'expression : LPAREN expression RPAREN'
    p[0] = p[2]

def p_expression_number(p):
    'expression : NUMBER'
    p[0] = p[1]

def p_expression_identifier(p):
    'expression : IDENTIFIER'
    p[0] = variables.get(p[1], 0)

def p_expression_string(p):
    'expression : STRING'
    p[0] = p[1]

def p_expression_concat(p):
    'expression : expression CONCAT expression'
    p[0] = str(p[1]) + str(p[3])

def p_error(p):
    print("Erro de sintaxe!")

# Construir o parser
parser = yacc.yacc()

# Função para executar a interpretação
def run_fca(data):
    parser.parse(data)
    if data:
        print("Variáveis finais:", variables)

# Função principal
def main():
    import sys
    if len(sys.argv) > 1:
        with open(sys.argv[1], 'r') as file:
            data = file.read()
    else:
        data = ""
        print("Insira os comandos (terminar com CTRL+D):")
        while True:
            try:
                line = input()
            except EOFError:
                break
            data += line + '\n'

    run_fca(data)

if __name__ == '__main__':
    main()