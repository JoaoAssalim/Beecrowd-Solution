ent = int(input())
n = 0
for i in range(1000):
    if n > 0 and n < ent:
        print(f'N[{i}] = {n}')
        n += 1
    else:
        n = 0
        print(f'N[{i}] = {0}')
        n += 1