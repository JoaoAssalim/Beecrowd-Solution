tentaS = 0
tentaB = 0
tentaA = 0
acertoS = 0
acertoB = 0
acertoA = 0

for i in range(int(input())):
    nome = input()
    TS, TB, TA = list(map(int, input().split()))
    AS, AB, AA = list(map(int, input().split()))
    tentaS += TS
    tentaB += TB
    tentaA += TA
    acertoS += AS
    acertoB += AB
    acertoA += AA

mediaS = (acertoS / tentaS) * 100
mediaB = (acertoB/ tentaB) * 100
mediaA = (acertoA / tentaA) * 100

print(f'Pontos de Saque: {mediaS:.2f} %.')
print(f'Pontos de Bloqueio: {mediaB:.2f} %.')
print(f'Pontos de Ataque: {mediaA:.2f} %.')
