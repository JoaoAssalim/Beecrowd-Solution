oper = input()
matriz = []

for i in range(12):
    matriz.append([])
    for j in range(12):
        num = float(input())
        matriz[i].append(num)

if oper == 'S':
    soma = 0
    indiceA = 1
    indiceB = 11
    for x in range(11,6,-1):
        for y in range(indiceA,indiceB):
            soma += matriz[x][y]
        indiceA += 1
        indiceB -= 1
    print(f'{soma:.1f}')
    
elif oper == 'M':
    soma = 0
    indiceA = 1
    indiceB = 11
    quant = 0
    for x in range(11,6,-1):
        for y in range(indiceA,indiceB):
            soma += matriz[x][y]
            quant += 1
        indiceA += 1
        indiceB -= 1
    media = soma / quant
    print(f'{media:.1f}')