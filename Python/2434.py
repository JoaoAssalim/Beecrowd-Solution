n, conta = list(map(int, input().split()))
valor = conta
for i in range(n):
    x = int(input())
    conta += x
    if conta < valor:
        valor = conta
print(valor)