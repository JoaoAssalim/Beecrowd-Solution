def maior(x):
    if len(x) < 4:
        x = x + "0"*(4-len(x))
    x = list(x)
    x.sort(reverse=True)
    return int("".join(x))

def menor(x):
    if len(x) < 4:
        x = x + "0"*(4-len(x))
    x = list(x)
    x.sort()
    return int("".join(x))
    

def krapekar(x):
    cnt = 0
    if x == 0:
        return -1
    while x != 6174:
        max = maior(str(x))
        min = menor(str(x))
        x = max - min
        cnt = cnt + 1
        
        if max == min:
            return -1
    
    return cnt

for i in range(int(input())):
    n = int(input())
    print(f'Caso #{i+1}: {krapekar(n)}')