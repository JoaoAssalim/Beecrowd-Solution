numeros = []
pos = 0
imp = 0
par = 0
neg = 0

for i in range(5):
    n = int(input())
    numeros.append(n)
    
for x in numeros:
    if x > 0:
        pos += 1
    elif x < 0:
        neg += 1
    if x %2 == 0:
        par += 1
    elif x%2 == 1:
        imp += 1
        
print(f'{par} valor(es) par(es)')
print(f'{imp} valor(es) impar(es)')
print(f'{pos} valor(es) positivo(s)')
print(f'{neg} valor(es) negativo(s)')