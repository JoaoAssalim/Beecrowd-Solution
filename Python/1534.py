while True:
    try:
        n = int(input())
        matriz = []
        one = 0
        two = n-1
        
        for i in range(n):
            matriz.append([])
            for u in range(n):
                matriz[i].append('')
        
        for cont1, r in enumerate(matriz):
            for cont, l in enumerate(r):
                if cont == two:
                    matriz[cont1][cont] = 2
                elif cont == one:
                    matriz[cont1][cont] = 1
                else:
                    matriz[cont1][cont] = 3
            one += 1
            two -= 1
                    
                    
        for mat in matriz:
            for item in mat:
                print(item, end='')
            print()
                    
    except EOFError:
        break
