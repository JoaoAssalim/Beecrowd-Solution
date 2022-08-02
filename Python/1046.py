ent = input().split()
inicio = int(ent[0])
fim = int(ent[1])

if inicio > fim:
    tempo = (24-inicio) + fim
    print(f'O JOGO DUROU {tempo} HORA(S)')
elif inicio < fim:
    tempo = fim - inicio
    print(f'O JOGO DUROU {tempo} HORA(S)')
elif inicio == fim:
    print('O JOGO DUROU 24 HORA(S)')