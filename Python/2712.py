for i in range(int(input())):
    placa = input()

    if len(placa) == 8 and placa[:3].isalpha() and placa.isupper() and placa[3] == '-' and placa[4:].isdigit():
        if placa.endswith('1') or placa.endswith('2'):
            print('MONDAY')
        elif placa.endswith('3') or placa.endswith('4'):
            print('TUESDAY')
        elif placa.endswith('5') or placa.endswith('6'):
            print('WEDNESDAY')
        elif placa.endswith('7') or placa.endswith('8'):
            print('THURSDAY')
        elif placa.endswith('9') or placa.endswith('0'):
            print('FRIDAY') 
    else:
        print('FAILURE')