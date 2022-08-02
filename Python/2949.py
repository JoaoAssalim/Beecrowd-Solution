hob = 0
hum = 0
elfo = 0
anao = 0
mago = 0

for i in range(int(input())):
    nome, classe = map(str, input().split())
    if classe == 'A': anao += 1
    elif classe == 'E': elfo += 1
    elif classe == 'H': hum += 1
    elif classe == 'M': mago += 1
    elif classe == 'X': hob += 1
    
print(f'{hob} Hobbit(s)')
print(f'{hum} Humano(s)')
print(f'{elfo} Elfo(s)')
print(f'{anao} Anao(s)')
print(f'{mago} Mago(s)')