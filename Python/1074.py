n = int(input())
lista = []

for i in range(n):
    num = int(input())
    lista.append(num)
for x in lista:
    if x > 0 and x % 2 == 0:
        print('EVEN POSITIVE')
    elif x < 0 and x % 2 == 0:
        print('EVEN NEGATIVE')
    elif x > 0 and x % 2 != 0:
        print('ODD POSITIVE')
    elif x < 0 and x % 2 != 0:
        print('ODD NEGATIVE')
    else:
        print('NULL')