caso = 1
while True:
    try:
        num = input()
        numeros = input().split()
        F = 0
        M = 0
        if caso > 1:
            print()
        
        for i in range(len(numeros)):
            if numeros[i] == num:
                if numeros[i+1] == 'F': F += 1
                else: M += 1
        print(f'Caso {caso}:')
        print(f'Pares Iguais: {M+F}')
        print(f'F: {F}')
        print(f'M: {M}')
        caso += 1
                
    except EOFError:
        break
    
