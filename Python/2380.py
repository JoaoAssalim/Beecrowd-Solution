def union(x, y):
    arr[find(x)] = find(y)
    
def find(x):
    parent = arr[x]
    while (parent != x):
        arr[x] = arr[parent]
        x = parent
        parent = arr[parent]
    
    return parent

n, m = list(map(int, input().split()))

arr = {i: i for i in range(1, n+1)}

for i in range(m):
    a, b, c = input().split()
    if a == "C":
        if find(int(b)) == find(int(c)):
            print("S")
        else:
            print("N")
    else:
        union(int(b), int(c))
