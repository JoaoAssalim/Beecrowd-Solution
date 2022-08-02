indice = int(input())
opcao = input().upper()
matriz = []
soma = 0

for coluna in range(12):
    lista_linha = []
    for linha in range(12):
        numero = float(input())
        lista_linha.append(numero)
    matriz.append(lista_linha)

for lista in matriz:
    soma += lista[indice]
    

if opcao == 'S':
    print(round(soma, 1))
else:
    media = (soma) / 12
    print(round(media, 1))