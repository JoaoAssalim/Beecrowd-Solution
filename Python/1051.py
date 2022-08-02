valor = float(input())

if valor <= 2000.00:
    print('Isento')
elif valor > 2000.00 and valor <= 3000.00:
    taxa = (valor-2000) * (8 / 100)
    print(f'R$ {taxa:.2f}')

elif valor > 3000.00 and valor <= 4500.00:
    taxa = (valor-3000) * (18 / 100) + ((8/100)*1000)
    print(f'R$ {taxa:.2f}')
else:
    taxa = (((8/100)*1000) + (18/100)*1500) + (valor-4500)*(28/100)
    print(f'R$ {taxa:.2f}')