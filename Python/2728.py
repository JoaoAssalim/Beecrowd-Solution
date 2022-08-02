while True:
    try:
        palavra = input().split('-')
        if len(palavra) == 5:
            length = 0
            for i in palavra:
                if length == 0:
                    if i[0] in 'cC' or i[-1] in 'cC':
                        length += 1
                elif length == 1:
                    if i[0] in 'Oo' or i[-1] in 'Oo':
                        length += 1
                elif length == 2:
                    if i[0] in 'Bb' or i[-1] in 'Bb':
                        length += 1
                elif length == 3:
                    if i[0] in 'Oo' or i[-1] in 'Oo':
                        length += 1
                elif length == 4:
                    if i[0] in 'Ll' or i[-1] in 'Ll':
                        length += 1
                
            if length == 5:
                print('GRACE HOPPER')
            else:
                print('BUG')
    except EOFError:
        break
