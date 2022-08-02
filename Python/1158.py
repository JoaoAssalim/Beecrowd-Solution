for i in range(int(input())):
    soma = 0
    cont = 0
    x, y = map(int, input().split())
    
    while cont < y:
        if x % 2 == 0:
            x += 1
        else:
            soma += x
            cont += 1
            x += 2
            
    print(soma)