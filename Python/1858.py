n = int(input())
pessoas = list(map(int, input().split()))
pos = 0
valor = 0
for i in range(n):
    if i == 0:
        pos = 1
        valor = pessoas[i]
    
    if pessoas[i] < valor:
        valor = pessoas[i]
        pos = i + 1
print(pos)
