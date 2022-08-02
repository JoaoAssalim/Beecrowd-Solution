num = int(input())
i = 1
while i <= num:
    if i % 2 == 0:
        print(f'{i}^2 = {i**2}')
        i += 2
    else:
        i += 1