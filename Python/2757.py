a = input()
b = input()
c = input()

if '0' in a[0]:
    a = str(int(a))
if '0' in b[0]:
    b = str(int(b))
if '0' in c[0]:
    c = str(int(c))

print(f'A = {a}, B = {b}, C = {c}')
espacoA = 10 - len(a)
espacoB = 10 - len(b)
espacoC = 10 - len(c)

print(f'A = {" "*espacoA}{a}, B = {" "*espacoB}{b}, C = {" "*espacoC}{c}')

if ('-' in a) or ('-' in b) or ('-' in c):
    if '-' in a:
        print(f'A = -{"0"*espacoA}{a[1:]},', end='')
    else:
        print(f'A = {"0"*espacoA}{a},', end='')
        
    if '-' in b:
        print(f' B = -{"0"*espacoB}{b[1:]},', end='')
    else:
        print(f' B = {"0"*espacoB}{b},', end='')
        
    if '-' in c:
        print(f' C = -{"0"*espacoC}{c[1:]}')
    else:
        print(f' C = {"0"*espacoC}{c}')
    
    
else:
    print(f'A = {"0"*espacoA}{a}, B = {"0"*espacoB}{b}, C = {"0"*espacoC}{c}')

print(f'A = {a}{" "*espacoA}, B = {b}{" "*espacoB}, C = {c}{" "*espacoC}')
