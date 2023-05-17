while True:
    a,b,c = list(map(int, input().split()))
    if a == b == c == 0:
        break
    
    if a == b == c:
        if a == b == c == 13:
            print("*")
        else:
            print(a+1, b+1, c+1)
        
    elif a == b or a == c or b == c:
        x = sorted([a,b,c])
        
        if x[0] == x[1] == 1:
            if x[2] < 13:
                print(1, 1, x[2]+1)
            else:
                print(x[0], x[1]+1, x[1]+1)
        else:
            if x[2] == 13 and x[1] != x[2]:
                print(1, x[1]+1, x[1]+1)
            elif x[0] == x[1]:
                print(x[0], x[0], x[2]+1)
            else:
                
                if x[0] + 1 == x[1]:
                    if x[1] + 1 > 13:
                        print(1,1,1)
                    else:
                        print(x[1], x[1], x[1]+1)
                else:
                    print(x[0]+1, x[1], x[1])
                
    else:
        print(1, 1, 2)
