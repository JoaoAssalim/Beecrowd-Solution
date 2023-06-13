s = [0,0,0,0]
for i in range(int(input())):
    p = input()
    palp = []
    for x in range(4):
        palp.append(input())
    v = input()
    venc = []
    for x in range(4):
        venc.append(input())
    
    for x in range(4):
        if venc[x] != palp[x]:
            s[x] += 1

m = max(s)
res = ''
for e, i in enumerate(s):
    if i == m:
        res += str(e+1) + " "

print(res[:-1])
