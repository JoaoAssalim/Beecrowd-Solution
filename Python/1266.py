from math import ceil
while True:
    n = int(input())
    if n == 0:
        break   
    
    postes = list(map(int, input().split()))
    
    fused = False
    qt = 0
    aux = 0
    
    if all(i == 0 for i in postes):
        print(int(ceil(n/2)))
    else:
        if postes[0] == 0 and postes[-1] == 0:
            postes.append(postes[0])
            postes = postes[1:]
            
        for i in range(n):
            if postes[i] == 0:
                aux += 1
            else:
                aux = 0
            
            if i == 1 and aux == 2:
                fused = True
            if aux == 2:
                qt += 1
                aux = 0
        
        if aux == 1 and postes[0] == 0 and fused == False:
            qt += 1
        print(qt)