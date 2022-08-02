forget = input()
numeros = input().split()

dois = 0
tres = 0
quatro = 0
cinco = 0

for n in numeros:
    if int(n) % 2 == 0:
        dois += 1
    if int(n) % 3 == 0:
        tres += 1
    if int(n) % 4 == 0:
        quatro += 1
    if int(n) % 5 == 0:
        cinco += 1

print(f'{dois} Multiplo(s) de 2')
print(f'{tres} Multiplo(s) de 3')
print(f'{quatro} Multiplo(s) de 4')
print(f'{cinco} Multiplo(s) de 5')