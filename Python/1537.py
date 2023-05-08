from math import factorial
while True:
    n = int(input())
    if n == 0:
        break
    
    if n == 3:
        print(1)
    else:
        res = 1
        for i in range(4, n+1):
            res = (res*i) % 1000000009
        
        print(res)
