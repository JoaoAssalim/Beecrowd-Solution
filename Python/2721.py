lista = ['Dasher', 'Dancer', 'Prancer', 'Vixen', 'Comet', 'Cupid', 'Donner', 'Blitzen', 'Rudolph']
A = input().split()
soma = 0

for i in A:
    soma += int(i)

soma = (soma - (int(soma/9)*9))- 1
print(lista[soma])
