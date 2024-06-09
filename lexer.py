import ply.lex as lex

# Tokens
tokens = [
    'VARIAVEL',
    'NUMERO',
    'LPAREN', 
    'RPAREN', 
    'MAIS',
    'MENOS',
    'MULTIPLICA',
    'DIVIDE',
    'IGUAL',
    'PONTOVIRGULA',
    'VIRGULA',
    'ESCREVER',
    'DOISPONTOS',
    'CONCATENACAO',
    'STRING',
    'STRINGESPECIAL',
    'ENTRADA',
    'ALEATORIO',
    'FUNCAO',
    'FIM'
]

t_ignore = ' \t\n'

t_LPAREN = r'\('
t_RPAREN = r'\)'
t_MAIS = r'\+'
t_MENOS = r'-'
t_MULTIPLICA = r'\*'
t_DIVIDE = r'/'
t_IGUAL = r'='
t_PONTOVIRGULA = r';'
t_VIRGULA = r','
t_DOISPONTOS = r':'
t_ESCREVER = r'ESCREVER'
t_CONCATENACAO = r'<>'
#t_STRING = r'\".*?\"|\'[^\']*\''
t_STRING = r'[\"\'](?!.*\#\{.*\}).*[\"\']'
# ATENCAO que é possivel fazer "...' 
#[\"\'] OU "" ou ''
#(?!.*#{.*}).* tudo menos a ordem ...#{...}...
t_STRINGESPECIAL = r'[\"\'].*\#\{.+\}.*[\"\']'
t_ENTRADA = r'ENTRADA'
t_ALEATORIO = r'ALEATORIO'
t_FUNCAO = r'FUNCAO'
t_FIM = r'FIM'

def t_NUMERO(t):
    r'\d+'  # Usa uma raw string aqui
    t.value = int(t.value)
    return t

# Regra de expressão regular para variáveis
def t_VARIAVEL(t):
    r'[a-z_][a-zA-Z0-9_]*[?!]*' 
    return t

#Nao é necessario adicionar no token list
# Regra para comentários
def t_COMENTARIOS(t):
    r'--.*'
    pass  # Ignorar o comentário

# Regra para comentários de múltiplas linhas
def t_INICIO_COMENTARIOS(t):
    r'{-.*'
    pass  # Ignorar o comentário

def t_FIM_COMENTARIOS(t):
    r'.*-}'
    pass  # Ignorar o comentário

def t_error(t):
    print(f"Caractere ilegal: {t.value[0]}")
    t.lexer.skip(1)

lexer = lex.lex()


