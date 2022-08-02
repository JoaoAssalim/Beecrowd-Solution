for i in range(int(input())):
    j1 = input()
    j2 = input()
    
    if j1 == 'ataque' and j2 == 'pedra':
        print('Jogador 1 venceu')
    elif j1 == 'pedra' and j2 == 'ataque':
        print('Jogador 2 venceu')
        
    elif j1 == 'pedra' and j2 == 'papel':
        print('Jogador 1 venceu')
    elif j1 == 'papel' and j2 == 'pedra':
        print('Jogador 2 venceu')
        
    elif j1 == 'papel' and j2 == 'ataque':
        print('Jogador 2 venceu')
    elif j1 == 'ataque' and j2 == 'papel':
        print('Jogador 1 venceu')
        
    elif j1 == 'ataque' and j2 == 'ataque':
        print('Aniquilacao mutua')
    elif j1 == 'pedra' and j2 == 'pedra':
        print('Sem ganhador')
    elif j1 == 'papel' and j2 == 'papel':
        print('Ambos venceram')
