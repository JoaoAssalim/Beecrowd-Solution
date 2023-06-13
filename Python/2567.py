while True:
    try:
        n = int(input())
        c = n
        if n % 2:
            c -= 1
        
        l = list(map(int, input().split()))
        s = 0
        
        l.sort()
        x, y = 0, n-1
        
        for i in range(int(c/2)):
            s += l[y] - l[x]
            y -= 1
            x += 1
        
        print(s)
    except EOFError:
        break
                