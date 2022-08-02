lista_numeros = []
numeros = set()
for i in range(int(input())):
    num = int(input())
    lista_numeros.append(num)
    numeros.add(num)
    
numeros = list(numeros)
for i in sorted(numeros):
    print(f'{i} aparece {lista_numeros.count(i)} vez(es)')