n = int(input())

notas = [100, 50, 20, 10, 5, 2, 1]

print(n)
for nota in notas:
    qnt_nota = n // nota
    print(f'{qnt_nota} nota(s) de R$ {nota},00')
    n -= qnt_nota * notas