for i in range(int(input())):
    pal = input().lower()
    
    if len(pal) == 3:
        if pal[0] == 'o' and pal[1] == 'n':
            print(1)
        elif pal[0] == 'o' and pal[2] == 'e':
            print(1)
        elif pal[1] == 'n' and pal[2] == 'e':
            print(1)
        else:
            print(2)
    else:
        print(3)
