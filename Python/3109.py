n = int(input())

l = list(range(n))

for i in range(int(input())):
    s = list(map(int, input().split()))
    if s[0] == 1:
        l[s[1]-1], l[s[2]-1] = l[s[2]-1], l[s[1]-1]
    else:
        c = 0
        chefe = s[1]-1
        while l[chefe] != s[1]-1:
            chefe = l[chefe]
            c += 1
        
        print(c)
