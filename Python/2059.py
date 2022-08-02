p, j1, j2, r, a = list(map(int, input().split()))

soma = j1 + j2
if r == 1 and a == 1:
    print('Jogador 2 ganha!')
else:
    if soma % 2 == 0 and p == 1:
        if r == 1 and a == 0:
            print('Jogador 1 ganha!')
        elif r == 0 and a == 0:
            print('Jogador 1 ganha!')
        elif r == 0 and a == 1:
            print('Jogador 1 ganha!')
            
    elif soma % 2 and p == 0:
        if r == 1 and a == 0:
            print('Jogador 1 ganha!')
        elif r == 0 and a == 0:
            print('Jogador 1 ganha!')
        elif r == 0 and a == 1:
            print('Jogador 1 ganha!')
            
    else:
        if r == 1 and a == 0:
            print('Jogador 1 ganha!')
        elif r == 0 and a == 0:
            print('Jogador 2 ganha!')
        elif r == 0 and a == 1:
            print('Jogador 2 ganha!')
        else:
            print('Jogador 2 ganha!')
