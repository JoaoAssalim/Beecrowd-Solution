maior = ''

while True:
    cc = ''
    pal = input().split()
    if '0' in pal[0]:
        break
    else:
        for i in pal:
            cc += f'{len(i)}-'
            if len(i) >= len(maior): maior = i
        print(cc[:-1])
print()
print(f'The biggest word: {maior}')