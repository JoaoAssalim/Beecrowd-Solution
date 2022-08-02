ver = 0
while True:
    try:
        pal = input()
        nova = ''
        
        for i in pal:
            nova += f'{i} '
        nova = nova[:-1]
        
        for i in range(len(pal)):
            print(nova)
            nova = f' {nova[:-2]}'
        
        print()
    except EOFError:
        break
    
