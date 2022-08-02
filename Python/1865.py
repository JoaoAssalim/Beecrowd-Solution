for i in range(int(input())):
    nome, forca = map(str, input().split())
    forca = int(forca)
    
    if nome == 'Thor' or nome == 'thor':
        print('Y')
    else:
        print('N')