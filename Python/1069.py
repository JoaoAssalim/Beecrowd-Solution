for i in range(int(input())):
    areia = input()
    conj = 0
    abre = 0
    
    for i in areia:
        if i == '<':
            abre += 1
        elif i == '>':
            if abre > 0:
                abre -= 1
                conj += 1
    print(conj)
