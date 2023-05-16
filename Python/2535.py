while True:
    try:
        total = 0
        n = int(input())
        for y in range(n):
            if y > 0:
                x = input()
            especie = input()
            raca = input().split()
            nome = input().split()
            
            
            ver = False
            if especie == 'cachorro':
                if len(nome) > 1:
                    for j in nome:
                        if raca[0][0] == j[0]:
                            ver = True
                            break
            if ver:
                total += 1
        print(total)
        x = input()
    except EOFError:
        break