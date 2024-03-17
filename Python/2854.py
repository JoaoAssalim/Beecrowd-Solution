def union(x, y):
    arr[find(x)] = find(y)

def find(x):
    pai = arr[x]
    
    while pai != x:
        arr[x] = arr[pai]
        x = pai
        pai = arr[pai]
    
    return pai

n, m = list(map(int, input().split()))
arr = {}

for i in range(m):
    a, b, c = input().split()
    if not a in arr:
        arr[a] = a
    if not c in arr:
        arr[c] = c
    
    union(a, c)

parents = []

for i in arr:
    if not parents:
        parents.append(i)
    ver = False
    for pai in parents:
        if find(pai) == find(i):
            ver = True
    
    if not ver:
        parents.append(i)

print(len(parents))
