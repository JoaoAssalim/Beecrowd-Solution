cont = 0
media = 0

while cont != 2:
    num = float(input())
    
    if num >= 0 and num <= 10:
        cont += 1
        media += num
    else:
        print('nota invalida')
print(f'media = {media/2:.2f}')