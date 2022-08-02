for i in range(int(input())):
    frase = input()
    soma = 0
    preparatorio = ''
    
    for i in frase:
        if i.isdigit():
            preparatorio += i
        else:
            if len(preparatorio) > 0:
                soma += int(preparatorio)
                preparatorio = ''
    if len(preparatorio) > 0:
        soma += int(preparatorio)
    print(soma)