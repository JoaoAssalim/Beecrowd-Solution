a = int(input())
b = int(input())
soma = 0
if a > b:
    if b < 0:
        b+=1
    for i in range(b, a):
        if i % 2 != 0:
            soma += i
            
else:
    if a < 0:
        a+=1
    for i in range(a, b):
        if i % 2 != 0:
            soma += i


print(soma)