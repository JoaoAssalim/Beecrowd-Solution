num = input().split()
cod = int(num[0])
quant = int(num[1])

if cod == 1:
    print(f'Total: R$ {quant*4:.2f}')
elif cod == 2:
    print(f'Total: R$ {quant*4.5:.2f}')
elif cod == 3:
    print(f'Total: R$ {quant*5:.2f}')
elif cod == 4:
    print(f'Total: R$ {quant*2:.2f}')
elif cod == 5:
    print(f'Total: R$ {quant*1.5:.2f}')