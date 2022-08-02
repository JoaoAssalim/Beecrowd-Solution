gaso = 0
alco = 0
dies = 0

while True:
    ent = int(input())
    if ent == 1:
        alco += 1
    elif ent == 2:
        gaso += 1
    elif ent == 3:
        dies += 1
    elif ent == 4:
        break
print('MUITO OBRIGADO')
print(f'Alcool: {alco}')
print(f'Gasolina: {gaso}')
print(f'Diesel: {dies}')