while True:
    a,b = list(map(int, input().split()))
    if a == b:
        break
    elif a > b:
        print('Decrescente')
    elif b > a:
        print('Crescente')