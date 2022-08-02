import math
x = input().split()
y = input().split()

x1 = float(x[0])
y1 = float(x[1])
x2 = float(y[0])
y2 = float(y[1])

dist = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
print(f'{dist:.4f}')