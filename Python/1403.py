while True:
    n, m = list(map(int, input().split()))
    if n == m == 0:
        break
    
    s = {}
    for i in range(n):
        l = list(map(int, input().split()))
        for j in l:
            if j in s:
                s[j] += 1
            else:
                s[j] = 1
    
    clas = [[s[key],key] for key in s.keys()]
    clas.sort(reverse=True)
    clas = clas[1:]
    maior = clas[0][0]
    l = []
    
    for i in clas:
        if i[0] == maior:
            l.append(i[1])
        else:
            break
        
    l.sort()
    for i in l:
        print(i, end=" ")
    print()

    