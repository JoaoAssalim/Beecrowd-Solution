ALFABETO = 'abcdefghijklmnopqrstuvwxyz'
for i in range(int(input())):
    contador = 0
    a, b = input().split()
    
    for indice, letra in enumerate(a):
        idx = ALFABETO.index(letra)
        while ALFABETO[idx] != b[indice]:
            contador += 1
            idx += 1
            if idx >= 26:
                idx -= 26
    print(contador)
