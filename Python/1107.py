while True:
    n, m = list(map(int, input().split()))
    if n == m == 0:
        break
    l = list(map(int, input().split()))
    c = 0
    
    for i in range(m):
        if i == 0:
            c += n - l[i]
        elif l[i] < l[i-1]:
            c += l[i-1] - l[i]
    print(c)
