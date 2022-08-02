caso = 1
while True:
    numeros = '0'
    try:
        num = int(input())
        for i in range(1, num+1):
            addnum = f' {str(i)}'
            numeros += f'{addnum * i}'
        
        n = numeros.split()
        
        if len(numeros) == 1:
            print(f'Caso {caso}: {len(n)} numero')
            print(numeros)
        else:
            print(f'Caso {caso}: {len(n)} numeros')
            print(numeros)
        caso += 1
        print()
    except EOFError:
        break