print('-'*39)
print('|  decimal  |  octal  |  Hexadecimal  |')
print('-'*39)

for i in range(16):
    octa = oct(i)[2:]
    hexa = hex(i)[2:].upper()
    
    strint1 = f'|      {int(i)}    '
    strint2 = f'|     {int(i)}    '
    stroct1 = f'|    {octa}    '
    stroct2 = f'|   {octa}    '
    strhex1 = f'|       {hexa}       |'
    strhex2 = f'|      {hexa}       |'
    
    if len(str(i)) == 1:
        print(f'{strint1}', end='')
    else:
        print(f'{strint2}', end='')
    if len(str(octa)) == 1:
        print(f'{stroct1}', end='')
    else:
        print(f'{stroct2}', end='')
    if len(str(hexa)) == 1:
        print(f'{strhex1}')
    else:
        print(f'{strhex2}')
        
print('-'*39)
