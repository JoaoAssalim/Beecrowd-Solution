n = int(input())
m = [0 for i in range(n)]
soma = 0
ver = True
x, y = 0, n-1

d1, d2 = 0, 0
for i in range(n):
    l = list(map(int, input().split()))
    d1 += l[x]
    d2 += l[y]
    x += 1
    y -= 1
    if i == 0:
        soma = sum(l)
    elif sum(l) != soma:
        ver = False
    
    for j in range(n):
        m[j] += l[j]

if all(i == soma for i in m) and ver and d1 == d2 == soma:
    print(soma)
else:
    print(-1)
