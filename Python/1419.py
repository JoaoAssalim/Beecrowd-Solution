while True:
    n = int(input())
    
    if n == 0:
        break
    
    m = list(map(int, input().split()))
    l = list(map(int, input().split()))
    ver = False
    xm = 0
    verm = 0
    xl = 0
    verl = 0
    antl = 0
    antm = 0
    
    for i in range(n):
        if i == 0:
            antl = l[i]
            antm = m[i]
            verm = 1
            verl = 1
        else:
            if m[i] == antm:
                verm += 1
            else:
                verm = 1
                antm = m[i]
                
            if l[i] == antl:
                verl += 1
            else:
                verl = 1
                antl = l[i]
            
            if verm == verl == 3:
                ver = True
            elif verm == 3 and verl != 3 and ver == False:
                ver = True
                xm += 30
            elif verm != 3 and verl == 3 and ver == False:
                ver = True
                xl += 30
                
        xm += m[i]
        xl += l[i]

    if xm == xl:
        print("T")
    elif xm > xl:
        print("M")
    else:
        print("L")