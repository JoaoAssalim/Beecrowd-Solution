val = input().split()
a = int(val[0])
b = int(val[1])
c = int(val[2])

maior = a
if b>maior:
    maior = b
elif c>maior:
    maior = c

print(f'{maior} eh o maior')