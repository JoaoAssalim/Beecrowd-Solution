while True:
    try:
        pessoas = int(input())
        qnt_imp = (pessoas/3)*2
        votos = input().split()
        qnt_votos = votos.count('1')
        
        if qnt_votos >= qnt_imp:
            print('impeachment')
        else:
            print('acusacao arquivada')
            
    except EOFError:
        break
