from math import gcd


while True:
    try:
        l = list(map(int, input().split()))
        l.sort(reverse=True)
        
        if (l[0]**2 == l[1]**2 + l[2]**2) and gcd(l[0], gcd(l[1], l[2])) == 1:
            print('tripla pitagorica primitiva')
        elif (l[0]**2 == l[1]**2 + l[2]**2):
            print('tripla pitagorica')
        else:
            print('tripla')
    except EOFError:
        break