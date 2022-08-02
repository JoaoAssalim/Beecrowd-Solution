while True:
    try:
        n, n1 = list(map(int, input().split()))
        total = 0
        for i in range(n1):
            dados = list(map(str, input().split()))
            qnt = dados[1:]
            data = dados[0]
            if all(ele == '1' for ele in qnt) and total == 0:
                total = data
        
        if total != 0:
            print(total)
        else:
            print('Pizza antes de FdI')
    except EOFError:
        break
