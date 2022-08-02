for i in range(int(input())):
    alt, esp, gal = map(int, input().split())
    
    if alt >= 200 and alt <= 300 and esp >= 50 and gal >= 150:
        print('Sim')
    else:
        print('Nao')