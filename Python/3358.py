for i in range(int(input())):
    nome = input()
    nome_teste = nome.lower()
    consoantes = 0
    conso = False
    
    for v in nome_teste:
        if v != "a" and v != "e" and v != "i" and v != "o" and  v !="u":
            consoantes += 1
        else:
            consoantes = 0
        if consoantes >=3:
            conso = True
            
    if conso:
        print(f'{nome} nao eh facil')
    else:
        print(f'{nome} eh facil')