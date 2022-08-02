for i in range(int(input())):
    pal = input()
    nova = ''
    
    for i in pal:
        if i.islower():
            nova += i
    print(nova[::-1])