while True:
    try:
        nova = ''
        while True:
            num = input()
            if not '#' in num: 
                nova += num
            else:
                nova += num
                break

        dec = int(nova[:-1], 2)
        if dec % 131071 == 0:
            print('YES')
        else:
            print('NO')
    except EOFError:
        break