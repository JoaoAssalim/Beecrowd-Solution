for i in range(int(input())):
    linguas = set()
    
    for y in range(int(input())):
        lingua = input()
        linguas.add(lingua)
        
    if len(linguas) > 1:
        print('ingles')
    else:
        for l in linguas:
            print(l)
