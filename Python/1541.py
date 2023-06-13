from math import floor, sqrt
while True:
    l = list(map(int, input().split()))
    if l[0] == 0:
        break
    a,b,c = l
    x = int(floor(sqrt((a*b)/c*100)))
    print(x)