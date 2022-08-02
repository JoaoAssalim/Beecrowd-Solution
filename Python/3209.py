for i in range(int(input())):
    tomadas = input().split()
    quant = int(tomadas[0]) - 1
    for c, x in enumerate(tomadas):
        tomadas[c] = int(x)
    total = sum(tomadas[1:])
    print(total-quant)
