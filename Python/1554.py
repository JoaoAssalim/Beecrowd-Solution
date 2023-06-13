for i in range(int(input())):
    n = int(input())
    bx, by = list(map(int, input().split()))
    near = 0
    dist = 999999999999999999999
    for j in range(n):
        x, y = list(map(int, input().split()))
        euc = (abs(bx-x)**2 + abs(by-y)**2)**0.5
        if euc < dist:
            dist = euc
            near = j + 1
    
    print(near)
