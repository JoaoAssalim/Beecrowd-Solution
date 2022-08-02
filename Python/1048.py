salario = float(input())

if salario > 0 and salario <= 400:
    reajuste = salario * 15 / 100
    print(f'Novo salario: {salario+reajuste:.2f}\nReajuste ganho: {reajuste:.2f}\nEm percentual: 15 %')
elif salario > 400 and salario <= 800:
    reajuste = salario * 12 / 100
    print(f'Novo salario: {salario+reajuste:.2f}\nReajuste ganho: {reajuste:.2f}\nEm percentual: 12 %')
elif salario > 800 and salario <= 1200:
    reajuste = salario * 10 / 100
    print(f'Novo salario: {salario+reajuste:.2f}\nReajuste ganho: {reajuste:.2f}\nEm percentual: 10 %')
elif salario > 1200 and salario <= 2000:
    reajuste = salario * 7 / 100
    print(f'Novo salario: {salario+reajuste:.2f}\nReajuste ganho: {reajuste:.2f}\nEm percentual: 7 %')
else:
    reajuste = salario * 4 / 100
    print(f'Novo salario: {salario+reajuste:.2f}\nReajuste ganho: {reajuste:.2f}\nEm percentual: 4 %')