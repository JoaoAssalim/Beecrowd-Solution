while True:
    a, b = list(map(str, input().split()))
    if int(a) == int(b) == 0:
        break
    else:
        carry = 0
        
        while len(a) < len(b):
            a = '0' + a
        while len(b) < len(a):
            b = '0' + b
        
        resto = 0
        for length in reversed(range(0, len(a))):
            if int(a[length]) + int(b[length]) + resto > 9 or int(a[length]) + int(b[length]) > 9:
                carry += 1
                resto = 1
            else:
                resto = 0
    if carry == 0: print(f'No carry operation.') 
    elif carry == 1: print(f'{carry} carry operation.')
    else: print(f'{carry} carry operations.')