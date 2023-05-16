while True:
    try:
        n = int(input())
        pal = []
        
        for i in range(n):
            pal.append(input())
        
        for i in range(int(input())):
            p = input()
            ind = 0
            m = 0
            
            for j in pal:
                if j[:len(p)] == p:
                    ind += 1
                    if len(j) > m:
                        m = len(j)
            if ind == 0:
                print(-1)
            else:
                print(ind, m)
        
    except EOFError:
        break