from math import factorial
primos = []
x = int(input())
numeros = input().split()

for n in numeros:
    n = int(n)
    mult=0
    
    if n >= 2:
        for count in range(2,n):
            if (n % count == 0):
                mult += 1
    else:
        mult += 1
    if(mult==0):
        primos.append(n)

for num in primos:
    print(f'{num}! = {factorial(int(num))}')
