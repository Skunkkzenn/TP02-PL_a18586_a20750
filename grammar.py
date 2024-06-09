import ply.yacc as yacc
from lexer import tokens

# Dicionarios para armazenar variaveis
variaveis : dict = {} 
funcoes : dict =  {}
funcoes_aux_ramos : dict =  {} 

# Ordem das operacoes
precedence = (
    ('left', 'MAIS', 'MENOS'),
    ('left', 'MULTIPLICA', 'DIVIDE'),
)

# Regras para o parser 
def p_inicio(p):
    'S : comandos'
    p[0] = p[1]

def p_comandos_multiplos(p):
    'comandos : comandos comando'
    p[0] = p[1] + [p[2]]

def p_comandos_unico(p):
    'comandos : comando'
    p[0] = [p[1]]

def p_comando(p):
    '''comando : decl_variavel
               | comando_escrever
               | comando_funcao'''
    p[0] = p[1]

def p_comando_escrever(p):
    '''comando_escrever : ESCREVER LPAREN expressao RPAREN PONTOVIRGULA
                        | ESCREVER LPAREN decl_variavel RPAREN PONTOVIRGULA'''        
    if p[1] == "ESCREVER":
        p[0] = p[3]
        try:
            if p[3] in variaveis.keys():
                p[0] = variaveis[p[3]]
        except:
            result = ', '.join([str(x) for x in p[3]])
            if result  in variaveis.keys():
                p[0] = variaveis[result]    
        print(p[3])

def p_comando_funcao(p):
    '''comando_funcao : FUNCAO VARIAVEL LPAREN parametros RPAREN VIRGULA DOISPONTOS decl_variavel 
                      | FUNCAO VARIAVEL LPAREN parametros RPAREN VIRGULA DOISPONTOS decl_variaveis_funcoes
                      | FUNCAO VARIAVEL LPAREN parametros RPAREN DOISPONTOS corpo FIM''' 
    #Alterado "comando" por "decl_variavel" (pq nao é para haver prints nas funcoes)
    if p[8] != "FIM" :
        if p[2] in variaveis:
            # Se a chave existir, juntar
            variaveis[p[2]].append((p[4], p[8]))
        else:
            # Se a chave não existir, criar
            variaveis[p[2]] = [(p[4], p[8])]

    elif p[8] == "FIM":
        if p[2] in variaveis:
            # Se a chave existir, juntar
            variaveis[p[2]].append((p[4], p[7]))
        else:
            # Se a chave não existir, criar
            variaveis[p[2]] = [(p[4], p[7])]     
    
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
    #Removido comando_escrever no enunciado diz para nao usar
    p[0] = p[1]
    
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
        my_string = ', '.join(p[5])
        p[0] = p[1]+p[2]+p[3]+p[4]+my_string+p[6]
        funcoes[p[1]] = p[3]+p[4]+my_string+p[6]
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
                     | VARIAVEL IGUAL VARIAVEL LPAREN parametros RPAREN PONTOVIRGULA
                     | VARIAVEL IGUAL LBRACKET parametros RBRACKET PONTOVIRGULA
                     | VARIAVEL IGUAL LBRACKET RBRACKET PONTOVIRGULA'''
    if len(p) == 3:
        p[0] = p[1]
    elif p[3] == "ENTRADA":

        user_input = input()
        variaveis[p[1]] = user_input
    elif p[3] == "ALEATORIO":
        import random
        aleatorio = random.randrange(p[5])
        variaveis[p[1]] = aleatorio
    elif len(p) == 8 and p[3] != "ALEATORIO":

        func_name = p[3]
        args = p[5]
        
        #Chama a funcao
        resultado  = chamarfuncao(func_name, args)  
        variaveis[p[1]] = resultado 
    elif p[3] == "[" and p[5] == "]":
        p[0] = p[4]
        variaveis[p[1]] = p[4]
    elif p[3] == "[" and  p[4] == "]":
        p[0] = p[4]
        variaveis[p[1]] = []
    else:

        p[0] = p[3]
        variaveis[p[1]] = p[3]

def chamarfuncao(func_name, args):

    if func_name in variaveis:
        previous_length = None
        contador = 0 
        valido = False
        for params, expression in variaveis[func_name]:   
            contador = contador +1
            current_length = len(params)                  
            if contador != 1 and previous_length != current_length:
                valido = True
            previous_length = current_length       
        if contador == 1 or valido:
            r = evaluate_function_call (func_name, args) 
            return r
        else:
            r = funcao_ramos(func_name, args) 
            return r

def funcao_ramos(func_name, args):
    import re
    if func_name in funcoes:
        if args not in funcoes[func_name]:
            funcoes[func_name].append(args)
        else:
            funcoes[func_name].append(args)
    else:
        funcoes[func_name] = [args]
    if func_name in variaveis:
        for params, expression in variaveis[func_name]:
            numero = None 
            if params != args:
                param_dict = {params[i]: args[i] for i in range(len(params))}
                if isinstance(expression, list): #Entre ser apenas uma expressao ou uma lista de expressoes
                    pattern = r'\(.+\)'  #para encontrar o que esta dentro das (,) os parametros
                    patternVariavel = r'^(.*?)=' #para encontrar tudo antes do (...) 
                    patternParenteses = r'\(|\)'      
                    for item in expression:
                        matches = re.findall(pattern, item)
                        parametros = ', '.join(matches)
                        if "aux" not in funcoes_aux_ramos:
                            funcoes_aux_ramos["aux"] = []
                        if parametros  not in funcoes_aux_ramos["aux"]  :        
                                                   
                            matchesNome = re.findall(patternVariavel, item)                           
                            my_string = ', '.join(matchesNome)
                            if matches:                                                                 
                                for param, arg in param_dict.items():
                                    result = re.sub(param,  str(arg), str(parametros)) 
                                    #item = matches.replace(param, str(arg) )                                    
                                result = re.sub(patternParenteses, '', result) # para remover os parenteses  
                                numero = eval(result)
                                result =[numero]
                                
                                funcoes_aux_ramos[my_string] = numero
                                numero = chamarfuncao(func_name,result)
                                                        
            else:
                                
                chaves_comuns = set(funcoes.keys()) & set(funcoes_aux_ramos.keys())
                equals_count = 0

                # Para contar quantas é que tem o "="
                for params, e in variaveis[func_name]:
                    if isinstance(e, int):
                        continue
                    for exp in e:
                        # Percorre cada posição na expressão
                        for char in exp:
                            # Se o caractere for '=', incrementa o contador
                            if char == '=':
                                equals_count += 1
                                                

                if len(chaves_comuns) != equals_count:
                    for chave in chaves_comuns:
                        if "chave" in funcoes_aux_ramos:
                            funcoes_aux_ramos["chave"].append(chave)
                        else:
                            funcoes_aux_ramos["chave"] = [chave] 
                                                
                        # Para igualar os valores das chaves
                        funcoes_aux_ramos[chave] = expression    
                        funcoes_aux_ramos["aux"] = funcoes[chave]
                    args = next(iter(funcoes[func_name]))
                else:
                    for chave in chaves_comuns:
                        if chave not in funcoes_aux_ramos["chave"]:
                            funcoes_aux_ramos[chave] = expression
                    break
                
        #Para a exresssao a+b
        for params, e in variaveis[func_name]:
            if isinstance(e, int):
                continue
            for exp in e:
                if '='  in exp:
                   continue

                letras_encontradas = re.findall(r'\b[a-zA-Z]\b', exp)
                for letra in letras_encontradas:
                    if letra in funcoes_aux_ramos:
                        valor = funcoes_aux_ramos[letra]
                        exp = exp.replace(letra, str(valor))
            res = exp
            return eval(res) 
                   
def evaluate_function_call(func_name, args):
    import re
    if func_name in variaveis:
        for params, expression in variaveis[func_name]:           
            if len(params) == len(args):
                    param_dict = {params[i]: args[i] for i in range(len(params))}
                    if isinstance(expression, list): #Entre ser apenas uma expressao ou uma lista de expressoes
                        expression_funcao = ""
                        numero = None  #Colocar em baixo casos possiveis
                        pattern = r'\(.+\)'  #para encontrar o que esta dentro das (,) os parametros
                        patternNome = r'^\w+(?=\()' #para encontrar tudo antes do (...) 
                        patternParenteses = r'\(|\)'      # pattern para remover os parenteses  
                        for item in expression:
                            matches = re.findall(pattern, item)
                            matchesNome = re.findall(patternNome, item)
                            if "=" in item:
                                for chave, valor in funcoes.items():
                                    resultado = chave + '=' + valor
                                    if resultado == item:
                                        for param, arg in param_dict.items():
                                            expression_funcao = valor.replace(param, str(arg))
                                            try:
                                                numero = eval(expression_funcao)
                                            except:
                                                numero = expression_funcao                                           
                                        
                            elif matches:                   
                                parametros = ', '.join(matches)
                                nome_funcao = ', '.join(matchesNome)                     
                                for param, arg in param_dict.items():
                                    result = re.sub(param,  str(arg), str(parametros)) 
                                    #item = matches.replace(param, str(arg) )
                                result = re.sub(patternParenteses, '', result) # para remover os parenteses  
                                result = result.split(',')
                                #result = re.sub(pattern,  result, item)  ver se é preciso mas acho que nao 
                                r = evaluate_function_call(nome_funcao, result)
                                
                                return r
                                
                                
                            else:
                                if numero != None:                     
                                    for param, arg in param_dict.items():
                                        expression_funcao = item.replace(param, str(numero))
                                else:
                                    for param, arg in param_dict.items():
                                        item = item.replace(param, str(arg) )
                                    return eval(item)
                        
                        
                        return eval(expression_funcao)

                    else:
                        expression_funcao = ""
                        numero = None  #Colocar em baixo casos possiveis
                        pattern = r'\(.+\)'  #para encontrar o que esta dentro dos (,) os parametros
                        patternNome = r'^\w+(?=\()' #para encontrar tudo antes do (...) 
                        #patternParenteses = r'[^\(\)]+' # pattern para remover os parenteses    
                        patternParenteses = r'\(|\)'     
                        matches = re.findall(pattern, expression)
                        matchesNome = re.findall(patternNome, expression)
                        #para FUNCAO area(c),: area(c, c);  EM BAIXO DO IF
                        if matches:                   
                                parametros = ', '.join(matches)
                                nome_funcao = ', '.join(matchesNome)                     
                                for param, arg in param_dict.items():
                                    result = re.sub(param,  str(arg), str(parametros)) 
                                    #item = matches.replace(param, str(arg) )
                                result = re.sub(patternParenteses, '', result) # para remover os parenteses  
                                result = result.split(',')
                                #result = re.sub(pattern,  result, item)  ver se é preciso mas acho que nao 
                                r = evaluate_function_call(nome_funcao, result)                            
                                return r
                        else:
                            for param, arg in param_dict.items():
                                expression = expression.replace(param, str(arg))
                            # Evaluate the expression
                            return eval(expression)        
                                        
                
    else:
        raise NameError(f"Function '{func_name}' is not defined")

def p_expressao_aritmetica(p):
    '''expressao : expressao MAIS expressao
                 | expressao MENOS expressao
                 | expressao MULTIPLICA expressao
                 | expressao DIVIDE expressao
                 | expressao CONCATENACAO expressao'''
    if isinstance(p[1], str) or isinstance(p[3], str):   #Basta 1 para converter tudo em string
        if p[2] == '+':
            p[0] = str(p[1]) + str("+")+ str(p[3])
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
        #print("") removido porque ha frases que nao têm p (caso dos comentarios)

    #else:
        #print("Erro sintático!")
      
# Construção do parser
parser = yacc.yacc()

def parse_code(code):
    parser.parse(code)
    return variaveis