while True:

    T = int(input())
    cal = 0
    idx = 1
    if T == 0:
        break
    else:
        for i in range(T):
            prod = input()
            
            if prod[idx-1].isdigit(): idx += 1
            
            if prod[idx:] == 'suco de laranja': cal += int(prod[:idx]) * 120
            elif prod[idx:] == 'morango fresco': cal += int(prod[:idx]) * 85
            elif prod[idx:] == 'mamao': cal += int(prod[:idx]) * 85
            elif prod[idx:] == 'goiaba vermelha': cal += int(prod[:idx]) * 70
            elif prod[idx:] == 'manga': cal += int(prod[:idx]) * 56
            elif prod[idx:] == 'laranja': cal += int(prod[:idx]) * 50
            elif prod[idx:] == 'brocolis': cal += int(prod[:idx]) * 34
        if cal >= 110 and cal <= 130:
            print(f'{cal} mg')
        elif cal < 110:
            print(f'Mais {110-cal} mg')
        elif cal > 130:
            print(f'Menos {cal-130} mg')