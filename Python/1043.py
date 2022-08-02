n = input().split()
a, b, c = float(n[0]), float(n[1]), float(n[2])

if abs(b - c) < a < (b + c) and (a - c) < b < (a + c) and (a - b) < c < (a + b):
    print(f'Perimetro = {a+b+c:.1f}')
else:
    area = ((a + b) / 2) * c
    print(f'Area = {area:.1f}')