n = float(input())

notas = [100, 50, 20, 10, 5, 2]
moedas = [1, 0.5, 0.25, 0.10, 0.05, 0.01]

print('NOTAS:')
for nota in notas:
    quant_nota = int(n/nota)
    print(f'{quant_nota} nota(s) de R$ {nota:.2f}')
    n -= nota * quant_nota
print('MOEDAS:')
for moeda in moedas:
    quant_moeda = int(n/moeda)
    print(f'{quant_moeda} moeda(s) de R$ {moeda:.2f}')
    n -= moeda * quant_moeda
    n = float(f'{n:.2f}')