while True:
    try:
        n = int(input())
        l = list(map(int, input().split()))
        f = list(map(int, input().split()))
        
        trocas = 0
        
        for i in range(n):
            if f[i] != l[i]:
                trocas += abs(l.index(f[i]) - i)
                l.remove(f[i])
                l.insert(i, f[i])
                
        print(trocas)
    except EOFError:
        break
