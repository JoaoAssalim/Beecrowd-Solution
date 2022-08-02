peca1 = input().split()
peca2 = input().split()

valor1 = float(peca1[-1])
valor2 = float(peca2[-1])

qnt1 = int(peca1[-2])
qnt2 = int(peca2[-2])

valor = (valor1*qnt1) + (valor2*qnt2)
print(f'VALOR A PAGAR: R$ {valor:.2f}')