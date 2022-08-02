total = 0
for i in range(int(input())):
    
    ped, qnt = map(int, input().split())
    
    if ped == 1001:
        total += qnt * 1.5
    elif ped == 1002:
        total += qnt * 2.5
    elif ped == 1003:
        total += qnt * 3.5
    elif ped == 1004:
        total += qnt * 4.5
    else:
        total += qnt * 5.5
        
print(f'{total:.2f}')