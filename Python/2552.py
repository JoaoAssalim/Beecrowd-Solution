while True:
    try:
        a, b = list(map(int, input().split()))
        m = []
        
        for i in range(a):
            l = list(map(int, input().split()))
            for j in range(b):
                if l[j] == 1:
                    l[j] = 9
            m.append(l)
        
        for i in range(a):
            for j in range(b):
                if m[i][j] == 9:
                    if i > 0:
                        if m[i-1][j] != 9:
                            m[i-1][j] += 1
                    if i < a-1:
                        if m[i+1][j] != 9:
                            m[i+1][j] += 1
                    if j > 0:
                        if m[i][j-1] != 9:
                            m[i][j-1] += 1
                    if j < b-1:
                         if m[i][j+1] != 9:
                            m[i][j+1] += 1   
        for i in range(a):
            s = ''
            for j in range(b):
                s += str(m[i][j])
            print(s)
    except EOFError:
        break
    