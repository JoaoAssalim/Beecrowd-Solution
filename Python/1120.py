while True:
    lista = []
    result = ''
    a, b = list(map(str, input().split()))

    if a == '0' and b == '0':
        break
    else:
        for i in b:
            if str(i) != a:
                lista.append(i)

        if len(lista) > 0:
            for x in lista:
                result += x
        else:
            result = 0
        print(int(result))