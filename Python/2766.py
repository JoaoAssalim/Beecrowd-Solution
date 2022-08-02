lista = []

while True:
    try:
        cdd = input()
        lista.append(cdd)
    except EOFError:
        break

print(lista[2])
print(lista[6])
print(lista[8])
