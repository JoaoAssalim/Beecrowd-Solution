while True:
    try:
        t = input()
        if t == 'esquerda':
            print('ingles')
        elif t == 'direita':
            print('frances')
        elif t == 'nenhuma':
            print('portugues')
        elif t == 'as duas':
            print('caiu')
    except EOFError:
        break