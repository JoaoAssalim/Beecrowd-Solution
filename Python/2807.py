length = int(input())
lista = []
text = ''
atual, proximo = 0, 1
for i in range(length+1):
    atual, proximo = atual+proximo, atual
    lista.append(proximo)

for x in sorted(lista[1:], reverse=True):
    text += f'{x} '
print(text[:-1])