for i in range(int(input())):
    ent = int(input())
    soma = 0

    for x in range(1, ent):
        if ent % x == 0:
            soma += x

    if ent == soma:
        print(f'{ent} eh perfeito')
    else:
        print(f'{ent} nao eh perfeito')