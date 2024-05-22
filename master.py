from grammar import parse_code, variables
import sys

def main():
    if len(sys.argv) > 1:
        # Se um arquivo foi passado como argumento
        with open(sys.argv[1], 'r', encoding='utf-8') as file:
            data = file.read()
        parse_code(data)
    else:
        # Se não, ler a entrada do terminal
        data = ""
        print("Insira comandos no terminal (finalize com ENTER + CTRL+Z e pressione enter):")
        while True:
            try:
                line = input()
            except EOFError:
                break
            data += line + '\n'
        parse_code(data)

    # Exibir as variáveis finais
    print("Variáveis finais:", variables)

if __name__ == '__main__':
    main()
