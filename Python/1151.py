length = int(input())
total = ''
atual, proximo = 0, 1
for i in range(length):
    atual, proximo = atual+proximo, atual
    total += f'{str(proximo)} '
print(total[0:-1])