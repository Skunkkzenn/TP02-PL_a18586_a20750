import ply.yacc as yacc
from lexer import tokens

# Variáveis para armazenar valores
variaveis : dict = {}

# Ordem operacoes
precedence = (
    ('left', 'MAIS', 'MENOS'),
    ('left', 'MULTIPLICA', 'DIVIDE'),
)
def p_inicio(p):
    'S : comandos'
    p[0] = p[1]
    #print(p[1])

def p_comandos_multiplos(p):
    'comandos : comandos comando'
    p[0] = p[1] + [p[2]]
    #print(p[1])
    #print(p[2])

def p_comandos_unico(p):
    'comandos : comando'
    p[0] = [p[1]]

def p_comando(p):
    '''comando : decl_variavel
               | comando_escrever
               | comando_funcao'''
    p[0] = [p[1]]
    #p[0] = p[1]
#def p_comandos_unico(p):
#    '''comando : comando
#                | decl_variavel'''
 #   p[0] = [p[1]]
 #   print(p[1])
# Parser rules
#def p_inicio(p):
#    '''S : comando
#         | decl_variavel'''
#    p[0] = p[1]

def p_comando_escrever(p):
    '''comando_escrever : ESCREVER LPAREN expressao RPAREN PONTOVIRGULA
                        | ESCREVER LPAREN decl_variavel RPAREN PONTOVIRGULA'''        
    
    if p[1] == "ESCREVER":
        p[0] = p[3]
        if p[3] in variaveis.keys():
            p[0] = variaveis[p[3]]
        print(p[3])

def p_comando_funcao(p):
    '''comando_funcao : FUNCAO expressao LPAREN parametros RPAREN VIRGULA DOISPONTOS expressao PONTOVIRGULA 
                      | FUNCAO expressao LPAREN parametros RPAREN DOISPONTOS corpo FIM'''
    if p[9] == "PONTOVIRGULA":
        variaveis[p[2]] = (p[4], p[8])   
    elif len(p) == 9:
        variaveis[p[2]] = (p[4], p[7]) 
    #p[0] = p[1]     funcao_nome 
def p_parametros(p):
    '''parametros : parametro
                  | parametro VIRGULA parametros'''
    if len(p) == 2:
        p[0] = [p[1]]
    else:
        p[0] = [p[1]] + p[3]

def p_parametro(p):
    'parametro :  expressao'
    p[0] = p[1]

def p_corpo(p):
    '''corpo : expressao
             | decl_variaveis   
             | expressao PONTOVIRGULA corpo'''
    if len(p) == 2:
        p[0] = [p[1]]
    else:
        p[0] = [p[1]] + p[3]
def p_decl_variavel(p):
    '''decl_variavel : VARIAVEL IGUAL expressao PONTOVIRGULA
                     | VARIAVEL IGUAL ENTRADA LPAREN RPAREN PONTOVIRGULA
                     | VARIAVEL IGUAL ALEATORIO LPAREN expressao RPAREN PONTOVIRGULA'''
    if p[3] == "ENTRADA":
        #print("TESTE")
        user_input = input()
        variaveis[p[1]] = user_input
    elif p[3] == "ALEATORIO":
        import random
        aleatorio = random.randrange(p[5])
        variaveis[p[1]] = aleatorio
    else:
        p[0] = p[3]
        variaveis[p[1]] = p[3]
    

def p_expressao_aritmetica(p):
    '''expressao : expressao MAIS expressao
                 | expressao MENOS expressao
                 | expressao MULTIPLICA expressao
                 | expressao DIVIDE expressao
                 | expressao CONCATENACAO expressao'''
    if isinstance(p[1], str) or isinstance(p[3], str):   #and nao para a funcao soma2
        if p[2] == '+':
            p[0] = str(p[1]) + str("+")+ str(p[3])
            #print(p[0])
        elif p[2] == '-':
            p[0] = str(p[1]) + str("-") + str(p[3])
        elif p[2] == '*':
            p[0] = str(p[1]) + str("*") +str(p[3])
        elif p[2] == '/':
            p[0] = str(p[1]) + str("/")+ str(p[3])
        elif p[2] == '<>':
            p[0] = str(p[1]) + str(p[3])
    else:
        if p[2] == '+':
            p[0] = p[1] + p[3]
        elif p[2] == '-':
            p[0] = p[1] - p[3]
        elif p[2] == '*':
            #print(p[1])
            #print(p[3])
            p[0] = p[1] * p[3]
        elif p[2] == '/':
            p[0] = p[1] / p[3]
        elif p[2] == '<>':
            p[0] = str(p[1]) + str(p[3])
    

def p_expressao_parentheses(p):
    'expressao : LPAREN expressao RPAREN'
    p[0] = p[2]

def p_expressao_numero(p):
    'expressao : NUMERO'
    p[0] = p[1]


def p_expressao_variavel(p):
    'expressao : VARIAVEL'
    if p[1] in variaveis:#####ISTO FOI PARA CONSEGUIR POR A DAR O MULT_3! DIREIRO
        p[0] = variaveis.get(p[1], 0)                                         
    else:
        p[0] = variaveis.get(0, p[1])

def p_expressao_string(p):
    'expressao : STRING'
    p[0] = variaveis.get(0, p[1][1:-1])  #[1:-1] para remover os simbolo "" ou ''

def p_expressao_string_especial(p):
    'expressao : STRINGESPECIAL'
    import re
    string_content = p[1][1:-1] 
    pattern = r'#{(.*?)}'  #\w -> [a-zA-Z0-9_]  da match e coloca a variavel dentro da list matches
    matches = re.findall(pattern, string_content)
    for match in matches:
        if match in variaveis:
            string_content = string_content.replace('#{'+match +'}', variaveis[match]) #substitui a palavra pela variavel
    p[0] = string_content

def p_error(p):
    if p:
        print("Erro sintático na posição: ", p.lexpos)
    #elif p == None:
        #print("") removido porque ha frases que nao tenham p (caso dos comentarios)

    #else:
        #print("Erro sintático!")

parser = yacc.yacc()

input_terminal = 'FUNCAO soma2(c) :\nc = c+1 ;\nc+1 ;\nFIM\n'
    
    
    
result = parser.parse(input_terminal)
#instructions = input_terminal.strip().split('\n')

#instructions = instructions[:-1]

#for instruction in instructions:
#    result = parser.parse(instruction)
    ##print(result)


print("Variáveis:", variaveis)

last_var = list(variaveis.keys())[-1]
print(f"Última variável atribuída: {last_var} = {variaveis[last_var]}")