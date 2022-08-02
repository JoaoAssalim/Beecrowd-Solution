import math

n = input().split()
num = [float(i) for i in n]

a, b, c = num[0], num[1], num[2]

try:
    x1 = (-b + math.sqrt(b**2-4*a*c))/(2*a)
    x2 = (-b - math.sqrt(b**2-4*a*c))/(2*a)
    
    print(f'R1 = {x1:.5f}\nR2 = {x2:.5f}')

except:
    print('Impossivel calcular')