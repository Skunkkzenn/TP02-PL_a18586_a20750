import ply.yacc as yacc
from lexer import tokens

# Variáveis para armazenar valores
variaveis : dict = {} 
funcoes : dict =  {}

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
    p[0] = p[1]
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
    '''comando_funcao : FUNCAO VARIAVEL LPAREN parametros RPAREN VIRGULA DOISPONTOS comando 
                      | FUNCAO VARIAVEL LPAREN parametros RPAREN DOISPONTOS corpo FIM'''
    if p[8] != "FIM" :
        variaveis[p[2]] = (p[4], p[8])
    elif p[8] == "FIM":
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
    '''corpo : funcoes 
             | funcoes corpo'''
    if len(p) == 2:
        p[0] = [p[1]]
    else:
        p[0] = [p[1]] + p[2]

def p_funcoes(p):
    '''funcoes : decl_variaveis_funcoes'''
    p[0] = p[1]
    #Removido comando_escrever no enunciado diz para nao usar

def p_decl_variaveis_funcoes(p):
    '''decl_variaveis_funcoes : VARIAVEL IGUAL expressao PONTOVIRGULA
                              | expressao PONTOVIRGULA
                              | VARIAVEL IGUAL ALEATORIO LPAREN expressao RPAREN PONTOVIRGULA
                              | VARIAVEL IGUAL VARIAVEL LPAREN parametros RPAREN PONTOVIRGULA
                              | VARIAVEL LPAREN parametros RPAREN PONTOVIRGULA'''
    if len(p) == 3:
        p[0] = p[1]
    elif p[3] == "ALEATORIO":
        import random
        aleatorio = random.randrange(p[5])
        variaveis[p[1]] = aleatorio
    elif len(p) == 8 and p[3] != "ALEATORIO":
        #p[0] = p[3]
        func_name = p[3]
        args = p[5]
        
        ################variaveis[p[1]] = (p[3], p[5]) 
        #resultado  = evaluate_function_call(func_name, args)  
        #variaveis[p[1]] = resultado
    elif len(p) == 6:
        my_string = ', '.join(p[3])
        p[0] = p[1]+p[2]+my_string+p[4]
    else:
        p[0] = p[1]+"="+p[3]
        funcoes[p[1]] = p[3]

def p_decl_variavel(p):
    '''decl_variavel : VARIAVEL IGUAL expressao PONTOVIRGULA
                     | expressao PONTOVIRGULA
                     | VARIAVEL IGUAL ENTRADA LPAREN RPAREN PONTOVIRGULA
                     | VARIAVEL IGUAL ALEATORIO LPAREN expressao RPAREN PONTOVIRGULA
                     | VARIAVEL IGUAL VARIAVEL LPAREN parametros RPAREN PONTOVIRGULA'''
    if len(p) == 3:
        p[0] = p[1]
    elif p[3] == "ENTRADA":
        #print("TESTE")
        user_input = input()
        variaveis[p[1]] = user_input
    elif p[3] == "ALEATORIO":
        import random
        aleatorio = random.randrange(p[5])
        variaveis[p[1]] = aleatorio
    elif len(p) == 8 and p[3] != "ALEATORIO":
        #p[0] = p[3]
        func_name = p[3]
        args = p[5]
        
        ################variaveis[p[1]] = (p[3], p[5]) 
        resultado  = evaluate_function_call(func_name, args)  
        variaveis[p[1]] = resultado
    else:

        p[0] = p[3]
        variaveis[p[1]] = p[3]
    
def evaluate_function_call(func_name, args):
    import re
    if func_name in variaveis:
        params, expression = variaveis[func_name]
        if len(params) != len(args):
            raise ValueError("Parameter count mismatch")
        # Create a dictionary for parameter substitution
        param_dict = {params[i]: args[i] for i in range(len(params))}
        #if isinstance(expression, dict):
        if isinstance(expression, list): #Entre ser apenas uma expressao ou uma lista de expressoes
            expression_funcao = ""
            numero = None  #Colocar em baixo casos possiveis
            pattern = r'\(.+\)'  #para encontrar o que esta dentro das (,) os parametros
            patternNome = r'^\w+(?=\()' #para encontrar tudo antes do (...) 
            #patternParenteses = r'[^\(\)]+' # pattern para remover os parenteses    
            patternParenteses = r'\(|\)'      
            for item in expression:
                matches = re.findall(pattern, item)
                matchesNome = re.findall(patternNome, item)
                if "=" in item:
                    for chave, valor in funcoes.items():
                        resultado = chave + '=' + valor
                        if resultado == item:
                            for param, arg in param_dict.items():
                                expression_funcao = valor.replace(param, str(arg))
                                numero = eval(expression_funcao)
                            #expressao_funcao = eval(funcoes[chave])
                               
                elif matches:                   
                    parametros = ', '.join(matches)
                    nome_funcao = ', '.join(matchesNome)                     
                    for param, arg in param_dict.items():
                        result = re.sub(param,  str(arg), str(parametros)) 
                        #item = matches.replace(param, str(arg) )
                        print(result)
                    result = re.sub(patternParenteses, '', result) # para remover os parenteses  
                    result = result.split(',')
                    #result = re.sub(pattern,  result, item)  ver se é preciso mas acho que nao 
                    r = evaluate_function_call(nome_funcao, result)
                    
                    return r
                    
                    
                    #fazer coisas: e chamar novamente a funcao....
                else:
                    if numero != None:                     
                        for param, arg in param_dict.items():
                            expression_funcao = item.replace(param, str(numero))
                            print(expression_funcao)
                    else:
                        for param, arg in param_dict.items():
                            item = item.replace(param, str(arg) )
                            print(item)
                        return eval(item)
            return eval(expression_funcao)

        else:
            for param, arg in param_dict.items():
                expression = expression.replace(param, str(arg))
                print(expression)
            # Evaluate the expression
            return eval(expression)        
    
            
            #c = eval(d['c'])
            
            #var =
            # Replace parameters in the expression
            
    else:
        raise NameError(f"Function '{func_name}' is not defined")

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

input_terminal = 'tmp_01 = 2*3+4 ;\na1_ = 12345 - (5191 * 15) ;\nidade_valida? = 1;\nmult_3! = a1_ * 3 ;\nvalor = 5;\nESCREVER(valor);   -- conteúdo de valor é apresentado\nESCREVER(365 * 2); -- 730\nESCREVER("Ola Mundo"); -- Olá, Mundo!\ncurso = "ESI";\nESCREVER("Olá, "<> curso); -- Olá, ESI\n{- exemplo interpolação de strings\n   Olá, EST IPCA! -}\nescola ="EST";\ninst = "IPCA";\nESCREVER ("Olá, #{escola} #{inst}!");\nvalor = ENTRADA();\nate10 = ALEATORIO(10);\nFUNCAO soma(a,b),: a+b ;\nFUNCAO soma2(c) :\nc = c+1 ;\nc+1 ;\nFIM\nseis = soma(4,2);\noito = soma2(seis);\nFUNCAO area_retangulo(a, b):\na * b;\nFIM\nFUNCAO area_quadrado(a):\n	area_retangulo(a, a);\nFIM\na = area_retangulo(10, 20);\nb = area_quadrado(30);'

    
    
    
result = parser.parse(input_terminal)
#instructions = input_terminal.strip().split('\n')

#instructions = instructions[:-1]

#for instruction in instructions:
#    result = parser.parse(instruction)
    ##print(result)


print("Variáveis:", variaveis)
print("Funcoes", funcoes)

last_var = list(variaveis.keys())[-1]
print(f"Última variável atribuída: {last_var} = {variaveis[last_var]}")