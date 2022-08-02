for i in range(int(input())):
    sup = float(input())
    dias = 0
    parar = 1
    while parar == 1:
        sup = sup / 2
        dias += 1

        if sup <= 1:
            parar = 0
    print(f'{dias} dias')