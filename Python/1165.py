from math import sqrt
for i in range(int(input())):
    p = int(input())
    if p == 1:
        print(f'{p} nao eh primo')
    elif p == 2 or p == 3:
        print(f'{p} eh primo')
    else:
        if p%2 == 0:
            print(f'{p} nao eh primo')
        else:
            n = 3
            r = p % n
            while r!=0 and n < sqrt(p):
                n += 2
                r = p % n
            if r!= 0:
                print(f'{p} eh primo')
            else:
                print(f'{p} nao eh primo')