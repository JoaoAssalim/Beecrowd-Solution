num = input().split()
a, b, c, d = int(num[0]), int(num[1]), int(num[2]), int(num[3])

if b > c and d > a and c + d > a + b:
    if a %2 == 0 and a > 0 and b > 0 and c > 0 and d > 0:
        print('Valores aceitos')
else:
    print('Valores nao aceitos') 