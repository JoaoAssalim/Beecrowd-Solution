for i in range(int(input())):
    win = ''
    sheldon, raj = list(map(str, input().split()))
    if sheldon == raj:
        win = ''
    elif sheldon == 'tesoura' and raj in ['papel', 'lagarto']:
        win = 'sheldon'
    elif sheldon == 'papel' and raj in ['pedra','Spock']:
        win = 'sheldon'
    elif sheldon == 'pedra' and raj in ['lagarto','tesoura']:
        win = 'sheldon'
    elif sheldon == 'lagarto' and raj in ['Spock','papel']:
        win = 'sheldon'
    elif sheldon == 'Spock' and raj in ['pedra','tesoura']:
        win = 'sheldon'
    else:
        win = 'raj'

    if win == 'sheldon': win = 'Bazinga!'
    elif win == 'raj': win = 'Raj trapaceou!'
    else: win = 'De novo!'
        
    print(f'Caso #{i+1}: {win}')
