jogos = 0
inter = 0
gremio = 0
empate = 0
while True:
    golsinter, golsgremio = map(int, input().split())
    jogos += 1
    if golsinter > golsgremio:
        inter += 1
    elif golsinter < golsgremio:
        gremio += 1
    elif golsinter == golsgremio:
        empate += 1
    
    print('Novo grenal (1-sim 2-nao)')
    novo = int(input())
    if novo != 1 and novo != 2:
        while novo != 1 and novo != 2:
            print('Novo grenal (1-sim 2-nao)')
            novo = int(input())
    if novo == 2:
        break
        
print(f'{jogos} grenais')
print(f'Inter:{inter}')
print(f'Gremio:{gremio}')
print(f'Empates:{empate}')
if inter > gremio:
    print('Inter venceu mais')
elif gremio > inter:
    print('Gremio vencer mais')
else:
    print('Nao houve vencedor')