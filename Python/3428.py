n = int(input())
l = list(map(int, input().split()))

f = {}
s = 0

for i in l:
    if i in f and f[i] > 0:
        f[i] -= 1
    else:
        s += 1
    
    if i-1 in f:
        f[i-1] += 1
    else:
        f[i-1] = 1

print(s)