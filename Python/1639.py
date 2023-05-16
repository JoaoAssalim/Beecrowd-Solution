while True:
    l = set()
    n = int(input())
    if n == 0:
        break
    l.add(n)
    while True:
        n = str(n**2)
        if len(n) < 8:
            n = "0" * (8-len(n)) + n
        n = int(n[2:6])
        if n in l:
            break
        l.add(n)
    print(len(l))
        