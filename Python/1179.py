par = []
impar = []

for i in range(15):
    ent = int(input())
    if ent % 2 == 0:
        par.append(ent)
    else:
        impar.append(ent)

    if len(par) == 5:
        c = 0
        for i in par:
            print(f'par[{c}] = {i}')
            c += 1
        par = []
        c = 0
    elif len(impar) == 5:
        c = 0
        for i in impar:
            print(f'impar[{c}] = {i}')
            c += 1
        impar = []
        c = 0
        
countimpar = 0
for x in impar:
    print(f'impar[{countimpar}] = {x}')
    countimpar += 1
countpar = 0
for y in par:
    print(f'par[{countpar}] = {y}')
    countpar += 1