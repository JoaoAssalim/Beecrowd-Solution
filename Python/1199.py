while True:
    num = input()
    decimal = int(num, 16)
    hexa_letras = ['a','b','c','d','e','f']
    if '0x' in num:
        print(decimal)
    else:
        num = int(num)
        if num < 0:
            break
        hexa = hex(num)
        hexa_novo = ''
        for i in hexa:
            if i.isalpha() and i in hexa_letras:
                hexa_novo += i.upper()
            else:
                hexa_novo += i
                
        print(hexa_novo)
