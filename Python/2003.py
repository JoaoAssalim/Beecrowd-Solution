while True:
    try:
        hora, minuto = list(map(int, input().split(':')))
        
        if hora <= 7:
            if hora == 7 and minuto >= 0:
                print(f'Atraso maximo: {minuto}')
            else:
                print('Atraso maximo: 0')
        else:
            atrasoH = hora - 7
            atrasoM = minuto
            
            if atrasoH == 0:
                atraso = atrasoM
            else:
                atraso = atrasoH*60 + atrasoM
            print(f'Atraso maximo: {atraso}')
            
    except EOFError:
        break
