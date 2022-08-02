while True:
    nova = ''
    try:
        pal = input()
        if any(i == 'l' for i in pal):
            pal = pal.replace('l', '1')
        if any(i == 'o' for i in pal):
            pal = pal.replace('o', '0')
        if any(i == 'O' for i in pal):
            pal = pal.replace('O', '0')
        if any(i == ',' for i in pal):
            pal = pal.replace(',', '')
        if any(i == ' ' for i in pal):
            pal = pal.replace(' ', '')
            
        if pal.isdigit() and int(pal) >= 0 and int(pal) <= 2147483647:
            print(int(pal))
        else:
            print('error')
    except EOFError:
        break