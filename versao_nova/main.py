from grammar import parse_code, variaveis
import sys

def main():
    if len(sys.argv) > 1:
        # Se um ficheiro foi passado como argumento
        with open(sys.argv[1], 'r', encoding='utf-8') as file:
            data = file.read()
        parse_code(data)
    else:
        # Se não, ler como input no terminal
        data = ""
        print("Insira comandos no terminal (finalize com ENTER + CTRL+Z e pressione enter):")
        while True:
            try:
                line = input()
            except EOFError:
                break
            data += line + '\n'
        parse_code(data)

    print("Variáveis:", variaveis)
    #print("Funcoes", funcoes)
    # Mostra as variáveis finais
    last_var = list(variaveis.keys())[-1]
    print(f"Última variável atribuída: {last_var} = {variaveis[last_var]}")

if __name__ == '__main__':
    main()
