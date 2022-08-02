while True:
    n1, n2 = map(int, input().split())
    
    if n1 <= 0 or n2<= 0:
        break
    else:
        if n1 > n2:
            soma = 0
            for i in range(n2, n1+1):
                print(i, end=' ')
                soma += i
            print(f'Sum={soma}')
        else:
            soma = 0
            for i in range(n1, n2+1):
                print(i, end=' ')
                soma += i
            print(f'Sum={soma}')