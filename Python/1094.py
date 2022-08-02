sapo = 0
coelho = 0
rato = 0
for i in range(int(input())):
    ent = input().split()
    if 'S' in ent:
        sapo += int(ent[0])
    elif 'C' in ent:
        coelho += int(ent[0])
    else:
        rato += int(ent[0])
total = sapo+coelho+rato
print(f'Total: {total} cobaias')
print(f'Total de coelhos: {coelho}')
print(f'Total de ratos: {rato}')
print(f'Total de sapos: {sapo}')
print(f'Percentual de coelhos: {(coelho/total)*100:.2f} %')
print(f'Percentual de ratos: {(rato/total)*100:.2f} %')
print(f'Percentual de sapos: {(sapo/total)*100:.2f} %')