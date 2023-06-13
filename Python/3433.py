cartas = {}
for i in range(1, 14):
    cartas[i] = 4

n = int(input())
joao = list(map(int, input().split()))
maria = list(map(int, input().split()))

Tj = 0
Tm = 0

for i in joao:
    if i >= 10:
        Tj += 10
    else:
        Tj += i
    cartas[i] -= 1
    
for i in maria:
    if i >= 10:
        Tm += 10
    else:
        Tm += i
    cartas[i] -= 1

ver = 0

x = list(map(int, input().split()))
for i in x:
    cartas[i] -= 1
    if i >= 10:
        Tj += 10
    else:
        Tj += i
        
    if i >= 10:
        Tm += 10
    else:
        Tm += i
ver = False
for i in cartas:
    if cartas[i] > 0:
        j = i
        if j > 10:
            j = 10
        if (Tm + j == 23 and Tj + j != 23) or (Tm + j <= 23 and Tj + j > 23) or (Tm + j == 23 and Tj + j == 23):
            print(i)
            ver = True
            break

if ver == False:
    print(-1)