while True:
    try:
        n, id = list(map(int, input().split()))
        quant = 0
        
        for i in range(n):
            idGame, game = list(map(int, input().split()))
            if idGame == id and game == 0:
                quant += 1
                
        print(quant)
    except EOFError:
        break
