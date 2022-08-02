while True:
    n,m = map(int, input().split())
    soma = 0
    novo = ''
    if n==m==0:
        break
    else:
        soma = n + m
        num_list = [x for x in str(soma)]
        for i in num_list:
            if i != '0':
                novo+=str(i)
    print(novo)