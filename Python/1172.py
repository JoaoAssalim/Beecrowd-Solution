lista = []

for i in range(10):
    ent = int(input())
    lista.append(ent)
conter = 0    
for x in lista:
    if lista[conter] <= 0:
        lista[conter] = 1
    conter += 1
conter = 0        
for y in lista:
    print(f'X[{conter}] = {y}')
    conter += 1