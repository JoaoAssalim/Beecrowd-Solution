while True:
    try:
        a = input()
        letra = ''
        sequencia = 0
        quantidade = 0

        a = a.split()
        for i in range(len(a)):
            if i == 0:
                letra = a[0][0].lower()
            elif letra == a[i][0].lower():
                sequencia += 1
            else:
                letra = a[i][0].lower()
                if sequencia > 0:
                    quantidade += 1
                sequencia = 0

        if sequencia > 0: quantidade +=1
        print(quantidade)
    except EOFError:
        break