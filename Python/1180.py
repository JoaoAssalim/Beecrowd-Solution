ind = int(input())
nums = input().split()
lista = []
for i in nums: lista.append(int(i))
menor = min(lista)
print(f'Menor valor: {int(menor)}')
index = lista.index(menor)
print(f'Posicao: {int(index)}')