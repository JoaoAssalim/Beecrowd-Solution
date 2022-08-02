natal = 360
meses = [31,29,31,30,31,30,31,31,30,31,30,31]
total = 0

while True:
    try:
        mes, dia = list(map(int, input().split()))
        total = natal - (sum(meses[:mes-1]) + meses[mes-1] - (meses[mes-1] - dia))
        
        if total == 1:
            print("E vespera de natal!")
        elif total < 0:
            print('Ja passou!')
        elif total == 0:
            print('E natal!')
        else:
            print(f'Faltam {total} dias para o natal!')
    except EOFError:
        break
        
