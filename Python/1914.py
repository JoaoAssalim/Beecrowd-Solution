for i in range(int(input())):
    frase = input().split()
    a, b = list(map(int, input().split()))
    if (a+b)%2 == 0:
        if frase[1] == 'PAR':
            print(frase[0])
        else:
            print(frase[2])
    else:
        if frase[1] == 'IMPAR':
            print(frase[0])
        else:
            print(frase[2])