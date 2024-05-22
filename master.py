from grammar import parse_code, variables

def main():

    import sys
    if len(sys.argv) > 1:
        with open(sys.argv[1], 'r', encoding='utf-8') as file:
            data = file.read()
        parse_code(data)
        print("Variáveis finais:", variables)
    else:
        data = ""
        print("Insira comandos no terminal (finalize com CTRL+Z e pressione enter):")
        while True:
            try:
                line = input()
            except EOFError:
                break
            data += line + '\n'
        parse_code(data)
        print("Variáveis finais:", variables)

if __name__ == '__main__':
    main()
