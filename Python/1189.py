oper = input()
matriz = []

for i in range(12):
    matriz.append([])
    for j in range(12):
        num = float(input())
        matriz[i].append(num)

soma = 0
quant = 0
for x in range(1,6):
    for y in range(x):
        soma += matriz[x][y]
        quant += 1

indB = 1
for x1 in range(10, 5, -1):
    for y1 in range(indB):
        soma += matriz[x1][y1]
        quant += 1
    indB += 1

if oper == 'S':
    print(f'{soma:.1f}')
elif oper == 'M':
    media = soma/quant
    print(f'{media:.1f}')
