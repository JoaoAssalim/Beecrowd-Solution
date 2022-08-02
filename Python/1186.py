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
    for x in range(11,0,-1):
        for y in range(indice,12):
            soma += matriz[x][y]
        indice += 1
    print(f'{soma:.1f}')

if opcao == 'M':
    soma = 0
    indice = 1
    quant = 0
    for x in range(11,0,-1):
        for y in range(indice,12):
            soma += matriz[x][y]
            quant += 1
        indice += 1
    media = soma / quant
    print(f'{media:.1f}')
