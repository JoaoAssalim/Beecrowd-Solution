while True:
    notas = [2, 5, 10, 20, 50, 100]
    A, B = list(map(int, input().split()))
    if A == B == 0:
        break
    total = B - A
    troco = False
    
    for x in notas:
        for y in notas:
            if (x+y)-total == 0:
                troco = True
    
    if troco:
        print('possible')
    else:
        print('impossible')
