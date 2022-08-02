veloz = []
while True:
    lista = []
    try:
        for i in range(int(input())):
            lista.append(float(input()))
        veloz.append(min(lista))
    except EOFError:
        break

for x in veloz:
    print(x)