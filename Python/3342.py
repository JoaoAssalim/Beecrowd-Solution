from re import A, T


n = int(input())
if n % 2 == 0:
    total = (n*n)/2
    print(f'{int(total)} casas brancas e {int(total)} casas pretas')
else:
    matriz = []
    for i in range(n):
        linha = []
        for x in range(n):
            if i % 2 == 0 and x % 2 == 0:
                linha.append('b')
            elif i % 2 == 0 and x % 2 == 1:
                linha.append('p')
            elif i % 2 == 1 and x % 2 == 0:
                linha.append('p')
            elif i % 2 == 1 and x % 2 == 1:
                linha.append('b')
        matriz.append(linha)
    a = 0
    b = 0
    for i in matriz:
        for item in i:
            if item == 'b': a += 1
            else: b += 1
    print(f'{int(a)} casas brancas e {int(b)} casas pretas')