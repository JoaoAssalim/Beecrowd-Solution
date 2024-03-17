def busca_binaria(lista, elemento):
    inicio = 0
    fim = len(lista) - 1

    while inicio <= fim:
        meio = (inicio + fim) // 2
        if lista[meio] == elemento:

            while meio >= 0 and lista[meio] == elemento:
                meio -= 1
            return meio + 1
        elif lista[meio] < elemento:
            inicio = meio + 1
        else:
            fim = meio - 1

    return -1

c = 1
while True:
    a,b = list(map(int, input().split()))
    if a == b == 0:
        break
    
    l = sorted(int(input()) for q in range(a))
    
    print(f"CASE# {c}:")
    c+=1

    for i in range(b):
        n = int(input())
        if busca_binaria(l, n) != -1:
            print(f"{n} found at {busca_binaria(l, n)+1}")
        else:
            print(f"{n} not found")
