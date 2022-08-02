for i in range(int(input())):
    pal = input()
    len_pal = len(pal) / 2
    
    parte1 = list(reversed(pal[:int(len_pal)]))
    parte2 = list(reversed(pal[int(len_pal):]))
    
    nova = ''
    for i in parte1: nova += i
    for x in parte2: nova += x
    print(nova)
