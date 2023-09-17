l = list(map(int, input().split()))
l.sort()

a,b,c,d = l

if a*d == b*c:
    print("S")
else:
    print("N")
