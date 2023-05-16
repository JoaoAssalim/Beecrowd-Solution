from math import floor
while True:
    n = int(input())
    if n == 0:
        break
    elif n == 1:
        print("X\n@")
    else:
        m = [['O' for i in range(n)] for j in range(n)]
        aux = [['O' for i in range(n)] for j in range(n)]
        m[int(floor(n/2))][int(floor(n/2))] = "X"
        aux[int(floor(n/2))][int(floor(n/2))] = "X"
        x, y = int(floor(n/2)), int(floor(n/2))
        dir = 1 #1 direita, 2 cima, 3 esquerda, 4 baixo
        for i in range(n*n):
            for j in m:
                print("".join(j))
            print("@")
            m[x][y] = "O"
            if dir == 1:
                if y+1 <= n-1:
                    y += 1
                    if aux[x-1][y] == "O":
                        dir = 2
                else:
                    dir = 2
            elif dir == 2:
                if x >= 0:
                    x -= 1
                    if aux[x][y-1] == "O":
                        dir = 3
                else:
                    dir = 3
            elif dir == 3:
                if y >= 0:
                    y -= 1
                    if aux[x+1][y] == "O":
                        dir = 4
                else:
                    dir = 4
            else:
                if x <= n-1:
                    x += 1
                    if aux[x][y+1] == "O":
                        dir = 1
                else:
                    dir = 1
            
            m[x][y] = 'X'
            aux[x][y] = 'X'
            
