for i in range(int(input())):
    texto = input().split()
    pattern = input()
    res = []
    
    for x in range(texto.count(pattern)):
        count = 0
        for y in range(texto.index(pattern)):
            count += len(texto[y]) + 1
        texto[texto.index(pattern)] = "+"*len(pattern)
        res.append(str(count))
    
    if len(res) > 0:
        print(" ".join(res)) 
    else:
        print(-1)
