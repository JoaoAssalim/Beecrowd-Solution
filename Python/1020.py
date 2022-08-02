n = int(input())
ano = n // 365
n -= ano*365
mes = n//30
n -= mes*30
print(f'{ano} ano(s)\n{mes} mes(es)\n{n} dia(s)')