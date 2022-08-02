um = 'adgjmpsvy'
dois = 'behknqtwz'
tres = 'cfilorux '

while True:
    try:
        for i in range(int(input())):
            letra = input().split()
            
            if letra[0] == '.':
                cont = letra.count('.')
                print(um[cont-1])
            elif letra[0] == '..':
                cont = letra.count('..')
                print(dois[cont-1])
            else:
                cont = letra.count('...')
                print(tres[cont-1])
    except EOFError:
        break
