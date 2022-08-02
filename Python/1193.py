for i in range(int(input())):
    num, base = list(map(str, input().split()))
    
    print(f'Case {i+1}:')
    if base == 'bin':
        dec = int(num, 2)
        hexa = str(hex(dec))
        print(f'{dec} dec')
        print(f'{hexa[2:]} hex')
    elif base == 'dec':
        hexa = str(hex(int(num)))
        bina = str(bin(int(num)))
        print(f'{hexa[2:]} hex')
        print(f'{bina[2:]} bin')
    elif base == 'hex':
        dec = int(num, 16)
        bina = str(bin(dec))
        print(f'{dec} dec')
        print(f'{bina[2:]} bin')
    print()