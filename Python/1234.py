while True:
    try:
        a = input()
        c = True
        nova = ''
        
        for i in a:
            if i == ' ':
                nova += ' '
                continue
            if c:
                c = False
                nova += i.upper()
            else:
                nova += i.lower()
                c = True
        print(nova)
    except EOFError:
        break