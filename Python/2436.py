n, m = list(map(int, input().split()))
x, y = list(map(int, input().split()))

x -= 1
y -= 1

mat = []

for i in range(n):
    mat.append(list(map(int, input().split())))
    
while True:
    troca = False
    
    if x < n-1 and not troca:
        if mat[x+1][y] == 1:
            troca = True
            x += 1
    if y < m-1 and not troca:
        if mat[x][y+1] == 1:
            troca = True
            y += 1
    if y > 0 and not troca:
        if mat[x][y-1] == 1:
            troca = True
            y -= 1
    if x > 0 and not troca:
        if mat[x-1][y] == 1:
            troca = True
            x -= 1
    mat[x][y] = 0
    
    if troca == False:
        break

print(x+1, y+1)
            
