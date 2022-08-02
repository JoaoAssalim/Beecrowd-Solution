for i in range(int(input())):
    a,b,c,d = list(map(int, input().split()))
    lista = [a,b]
    listb = [c,d]
    if max(lista) < max(listb) and min(lista) < min(listb):
        print('S')
    else:
        print('N')
