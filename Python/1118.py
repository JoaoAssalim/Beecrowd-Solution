def media():
    c = 0
    nota = 0
    while c < 2:
        n = float(input())
        if n >= 0 and n <= 10:
            c += 1
            nota += n
        else:
            print('nota invalida')
    c = 0
    print(f'media = {nota/2:.2f}')
    nota = 0
    

media()
while True:
    print('novo calculo (1-sim 2-nao)')
    ent = int(input())
    if ent == 2:
        break
    elif ent == 1:
        media()
    else:
        pass