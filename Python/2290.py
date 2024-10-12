while True:
    try:
        n = int(input())
        if n == 0:
            break
        l = list(map(int, input().split()))
        d = {}
        
        for i in l:
            if i in d:
                d[i] += 1
            else:
                d[i] = 1
        
        d = sorted([i for i in d if d[i] % 2])
        print(d[0], d[1])
    except EOFError:
        break
