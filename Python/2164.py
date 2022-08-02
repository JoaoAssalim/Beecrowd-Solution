length = int(input())
atual, proximo = 0, 1
for i in range(length+1):
    atual, proximo = atual+proximo, atual
print(f'{proximo:.1f}')