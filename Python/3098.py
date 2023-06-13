def encontrar_maior_plindromo(palavra):
    tamanho = len(palavra)
    matriz = [[0] * tamanho for _ in range(tamanho)]

    for i in range(tamanho):
        matriz[i][i] = 1 if palavra[i] != 'a' else 0

    for sublen in range(2, tamanho + 1):
        for i in range(tamanho - sublen + 1):
            j = i + sublen - 1
            if palavra[i] == palavra[j] and palavra[i] != 'a' and palavra[j] != 'a':
                matriz[i][j] = matriz[i + 1][j - 1] + 2
            else:
                matriz[i][j] = max(matriz[i + 1][j], matriz[i][j - 1])

    return matriz[0][tamanho - 1]


palavra = input()
resultado = encontrar_maior_plindromo(palavra)
print(resultado)
