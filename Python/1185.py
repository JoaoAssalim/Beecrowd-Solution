opcao = input()
matriz = []

for i in range(12):
    matriz.append([])
    for j in range(12):
        num = float(input())
        matriz[i].append(num)

if opcao == 'S':
    soma = 0
    indice = 1
    for x in range(10,-1,-1):
        for y in range(0,indice):
            soma += matriz[x][y]
        indice += 1
    print(f'{soma:.1f}')

if opcao == 'M':
    soma = 0
    indice = 1
    quant = 0
    for x in range(10,-1,-1):
        for y in range(0,indice):
            soma += matriz[x][y]
            quant += 1
        indice += 1
    media = soma / quant
    print(f'{media:.1f}')