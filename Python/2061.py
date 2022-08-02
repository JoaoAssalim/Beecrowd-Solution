abas, acoes = list(map(int, input().split()))

for i in range(acoes):
    ac = input()
    if ac == 'fechou':
        abas += 1
    elif ac == 'clicou':
        abas -= 1
print(abas)