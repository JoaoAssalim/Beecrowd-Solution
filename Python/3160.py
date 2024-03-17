a1 = input().split()
a2 = input().split()
ind = input()

if ind == "nao":
    a1 = a1 + a2
    print(" ".join(a1))
else:
    n = []
    ver = -1
    for e, i in enumerate(a1):
        if i == ind:
            ver = e
            break
        if ver == -1:
            n.append(i)
    
    if ver != -1:
        for i in a2:
            n.append(i)
        for i in range(ver, len(a1)):
            n.append(a1[i])
    print(" ".join(n))
