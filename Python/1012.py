val = input().split()
a = float(val[0])
b = float(val[1])
c = float(val[2])

area = a*c/2
raio = 3.14159 * (c**2)
trap = (a+b)*c/2
quad = b*b
ret = a*b

print(f'TRIANGULO: {area:.3f}')
print(f'CIRCULO: {raio:.3f}')
print(f'TRAPEZIO: {trap:.3f}')
print(f'QUADRADO: {quad:.3f}')
print(f'RETANGULO: {ret:.3f}')
