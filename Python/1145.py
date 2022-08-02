x, y = map(int, input().split())
counter = 1

while counter <= y:
    aux = ''
    for i in range(x):
        aux += f'{counter} '
        counter += 1
    print(aux[:-1])