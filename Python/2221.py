for i in range(int(input())):
    B = int(input())
    Ai, Di, Li = list(map(int, input().split()))
    golpe1 = (Ai + Di) / 2
    if Li % 2 == 0: golpe1 += B
    Ay, Dy, Ly = list(map(int, input().split()))
    golpe2 = (Ay + Dy) / 2
    if Ly % 2 == 0: golpe2 += B
     
    if golpe1 > golpe2:
         print('Dabriel')
    elif golpe2 > golpe1:
        print('Guarte')
    else:
        print('Empate')
