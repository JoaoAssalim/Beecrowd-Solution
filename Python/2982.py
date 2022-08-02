gastos = 0
valores = 0

for i in range(int(input())):
    opt, val = list(map(str, input().split()))
    if opt == 'G': gastos += int(val)
    else: valores += int(val)
    
if valores > gastos:
    print('A greve vai parar.')
else:
    print('NAO VAI TER CORTE, VAI TER LUTA!')
