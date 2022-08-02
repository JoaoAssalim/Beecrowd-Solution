while True:
    try:
        ent = int(input())
        if ent == 0:
            print('vai ter copa!')
        else:
            print('vai ter duas!')

    except EOFError:
        break