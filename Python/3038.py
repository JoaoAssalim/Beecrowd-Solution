while True:
    try:
        palavra = input()
        if '@' in palavra: palavra = palavra.replace('@', 'a')
        if '&' in palavra: palavra = palavra.replace('&', 'e')
        if '!' in palavra: palavra = palavra.replace('!', 'i')
        if '*' in palavra: palavra = palavra.replace('*', 'o')
        if '#' in palavra: palavra = palavra.replace('#', 'u')
        
        print(palavra)
    except EOFError:
        break