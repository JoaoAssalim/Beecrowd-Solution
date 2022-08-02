for i in range(int(input())):
    ent1, ent2 = list(map(int, input().split()))
    conta = 0

    if ent1 > ent2:
        for i in range(ent2+1, ent1):
            if i % 2:
                conta += i
    else:
        for i in range(ent1+1, ent2):
            if i % 2:
                conta += i

    print(conta)