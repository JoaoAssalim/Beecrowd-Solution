while True:
    x,y = list(map(int, input().split()))
    
    if x == 0 or y == 0:
        break
    else:
    
        if x > 0:
            if y > 0:
                print('primeiro')
            else:
                print('quarto')
        else:
            if y > 0:
                print('segundo')
            else:
                print('terceiro')