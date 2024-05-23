# lexer.py
import ply.lex as lex
import codecs

# Lista de tokens
tokens = [
    'ESCREVER',      # print
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
    'CONCAT',        # <>
    'EQUALS',        # =
    'COLON_EQUALS',  # :=
    'OPEN_BRACE',    # {
    'CLOSE_BRACE',   # }
    'COMMA',         # ,
    'COLON',         # :
    'ENTRADA',       # input
    'ALEATORIO'      # random
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
t_CONCAT = r'<>'
t_EQUALS = r'='
t_OPEN_BRACE = r'{'
t_CLOSE_BRACE = r'}'
t_COMMA = r','
t_COLON = r':'
t_COLON_EQUALS = r':='

def t_ESCREVER(t):
    r'ESCREVER'
    return t

def t_READ(t):
    r'READ'
    return t

def t_NUMERO(t):
    r'\d+'
    t.value = int(t.value)
    return t

def t_STRING(t):
    r'"([^\\"]|\\[\\"]|\\[uU][0-9a-fA-F]{4})*"'
    t.value = codecs.escape_decode(t.value[1:-1].encode())[0].decode('utf-8')
    return t

# Regra de expressão regular para variáveis
def t_VARIABLE(t):
    r'[a-zA-Z_][a-zA-Z0-9_]*[\?\!]?|[^\x00-\x7F]+'
    return t

# Regra para comentários
def t_COMMENT(t):
    r'\-\-.*'
    pass  # Ignorar o comentário

# Regra para comentários de múltiplas linhas
def t_multiline_comment(t):
    r'\{\-([^{}]*|(\{[^{}]*\}))*\-\}'
    pass  # Ignorar o comentário

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

if __name__ == '__main__':
    # Teste para imprimir tokens
    code = '''
    tmp_01 := 2*3+4 ;
    a1_ := 12345 - (5191 * 15) ;
    idade_valida? := 1;
    mult_3! := a1_ * 3 ;
    '''
    print("Tokens:")
    print_tokens(code)