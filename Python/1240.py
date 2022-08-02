for i in range(int(input())):
    a,b = map(str, input().split())
    if a.endswith(b):
        print('encaixa')
    else:
        print('nao encaixa')