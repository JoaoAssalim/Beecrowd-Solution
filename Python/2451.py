n = int(input())
m = []
c = 0
dir = 1
aux = 0
ver = False
for i in range(n):
    s = input()
    if dir == 1:
        for j in range(n):
            if s[j] == 'A':
                if aux > c:
                    c = aux
                aux = 0
                
            elif s[j] == 'o':
                aux += 1
    else:
        for j in range(n-1, -1, -1):
            if s[j] == 'A':
                if aux > c:
                    c = aux
                aux = 0
            elif s[j] == 'o':
                aux += 1
    
    if dir == 1:
        dir = 0
    else:
        dir = 1

if aux > c:
    c = aux
print(c)
