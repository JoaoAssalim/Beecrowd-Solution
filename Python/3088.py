while True:
    try:
        palavra = input()
        nova = ''
        
        for i in palavra:
            if i == '.' or i == ',':
                if len(nova) > 0:
                    if nova[-1] == ' ':
                        nova = nova[:-1]
                        nova += i
                    else:
                        nova += i
                else:
                    nova += i
            else:
                nova += i
        print(nova)
        
    except EOFError:
        break
