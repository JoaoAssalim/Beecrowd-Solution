n = int(input())
atual, cont = 0, 0

for i in range(n):
    num = int(input())
    if i == 0:
        atual = num
        cont += 1
    elif atual != num:
        atual = num
        cont += 1

print(cont)
