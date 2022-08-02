for i in range(int(input())):
    hora, min, opt = map(str, input().split())
    if int(hora) < 10:
        hora = f'0{hora}'
    if int(min) < 10:
        min = f'0{min}'
        
    if opt == '1':
        print(f'{hora}:{min} - A porta abriu!')
    else:
        print(f'{hora}:{min} - A porta fechou!')