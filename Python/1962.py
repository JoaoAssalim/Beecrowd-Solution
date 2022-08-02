for i in range(int(input())):
    ano_atual = 2015
    ano = int(input())
    
    if ano >= ano_atual:
        print(f'{(ano-ano_atual)+1} A.C.')
    else:
        print(f'{ano_atual-ano} D.C.')