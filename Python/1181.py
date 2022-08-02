indice = int(input())
opcao = input().upper()
matriz = []

for coluna in range(12):
    lista_linha = []
    for linha in range(12):
        numero = float(input())
        lista_linha.append(numero)
    matriz.append(lista_linha)
    

if opcao == 'S':
    print(round(sum(matriz[indice]),1))
else:
    media = (sum(matriz[indice])) / 12
    print(round(media, 1))