while True:
    try:
        equ = input()
        
        if 'J' in equ:
            print(eval(equ[:-2]))
        elif 'L' in equ:
            eqo = equ.split('+')
            result = eqo[-1].split('=')
            print(int(result[-1]) - int(eqo[0]))
        else:
            eq = equ.split('+')
            resulte = eq[-1].split('=')
            print(int(resulte[1]) - int(resulte[0]))
    except EOFError:
        break
