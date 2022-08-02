distancias = []
while True:
    try:
        Nome = input()
        distancia = int(input())
        distancias.append(distancia)
    except EOFError:
        break
    
print(f'{sum(distancias)/len(distancias):.1f}')
