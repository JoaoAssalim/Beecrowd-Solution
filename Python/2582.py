for i in range(int(input())):
    a,b = map(int,(input().split()))
    
    soma = a + b
    if soma > 10:
        while soma <= 10:
            soma -= 10
    if soma == 0:
        print('PROXYCITY')
    elif soma == 1:
        print('P.Y.N.G.')
    elif soma == 2:
        print('DNSUEY!')
    elif soma == 3:
        print('SERVERS')
    elif soma == 4:
        print('HOST!')
    elif soma == 5:
        print('CRIPTONIZE')
    elif soma == 6:
        print('OFFLINE DAY')
    elif soma == 7:
        print('SALT')
    elif soma == 8:
        print('ANSWER!')
    elif soma == 9:
        print('RAR?')
    elif soma == 10:
        print('WIFI ANTENNAS')