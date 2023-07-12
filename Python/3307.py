from math import sqrt
ver = 0
azul = 0
ama = 0
for i in range(int(input())):
    n = int(input())
    r = sqrt(n/(4*3.14))
    if r < 12:
        print(f'vermelho = R$ {n*0.09:.2f}')
    elif r <= 15:
        print(f'azul = R$ {n*0.07:.2f}')
    else:
        print(f'amarelo = R$ {n*0.05:.2f}')
