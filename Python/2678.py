while True:
    try:
        frase = input().upper()
        nova = ''
        for i in frase:
            if i.isdigit():
                nova += i
            elif i.isalpha():
                if i == 'A' or i == 'B' or i == 'C': nova += '2'
                elif i == 'D' or i == 'E' or i == 'F': nova += '3'
                elif i == 'G' or i == 'H' or i == 'I': nova += '4'
                elif i == 'J' or i == 'K' or i == 'L': nova += '5'
                elif i == 'M' or i == 'N' or i == 'O': nova += '6'
                elif i == 'P' or i == 'Q' or i == 'R' or i == 'S': nova += '7'
                elif i == 'T' or i == 'U' or i == 'V': nova += '8'
                elif i == 'W' or i == 'X' or i == 'Y' or i == 'Z': nova += '9'

            else:
                if i == '*' or i == '#': nova += i
        print(nova)
    
    except EOFError:
        break