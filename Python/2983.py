from math import sqrt

lista = []
primos = []
num = 0
p = ''
for i in range(int(input())):
    n = int(input())
    if n not in lista:
        lista.append(n)
    
for i in sorted(lista):
    if i == 1:
        pass
    elif i == 2 or i == 3:
        primos.append(i)
        num += 1
    else:
        if i == 1:
            pass
        elif i%2 == 0:
            pass
        else:
            x = 3
            r = i % x
            while r!=0 and x < sqrt(i):
                x += 2
                r = i % x
            if r!= 0:
                primos.append(i)
                num += 1
            else:
                pass
print(len(primos))
if len(primos) == 0:
    print()
else:
    for z in primos: p += f'{z}, '
    p = p[:-2]
    p += '.'
    print(p)