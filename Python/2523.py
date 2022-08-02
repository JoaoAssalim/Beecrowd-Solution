while True:
    try:
        letras = input()
        quant = int(input())
        indices = input().split()
        nova = ''
        for l in indices:
            nova += letras[int(l)-1]
        print(nova)
    except EOFError:
        break