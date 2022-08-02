while True:
    try:
        lista_codigos = []
        for i in range(int(input())):
            codigo = input()
            lista_codigos.append(codigo)
        for x in sorted(lista_codigos):
            print(x)
    except EOFError:
        break