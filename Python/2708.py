jipes = 0
pessoas = 0

while True:
    info = input()
    
    if 'ABEND' in info:
        break
    
    info = info.split()
    p = info[-1]
    viagem = info[0]
    
    if viagem == 'SALIDA':
        jipes += 1
        pessoas += int(p)
    else:
        jipes -= 1
        pessoas -= int(p)
print(pessoas)
print(jipes)
