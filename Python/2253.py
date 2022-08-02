while True:
    try:
        maiusculas = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        minusculas = 'abcdefghijklmnopqrstuvwxyz'
        numero = 0
        digitoMaiusculo = 0
        digitoMinusculo = 0
        digitoInvalido = 0
        senha = input()
        if len(senha) >= 6 and len(senha) <= 32:
            for item in senha:
                if item.islower() and item in minusculas:
                    digitoMinusculo += 1
                elif item.upper() and item in maiusculas:
                    digitoMaiusculo += 1
                elif item.isdigit():
                    numero += 1
                else:
                    digitoInvalido += 1
            
            if digitoMaiusculo > 0 and digitoMinusculo > 0 and numero > 0 and digitoInvalido == 0:
                print('Senha valida.')
            else:
                print('Senha invalida.')
        else:
            print('Senha invalida.')
    except EOFError:
        break