fileira_1 = "`1234567890-="
fileira_2 = r"QWERTYUIOP[]\\"
fileira_3 = "ASDFGHJKL;'"
fileira_4 = "ZXCVBNM,./"
while True:
    try:
        frase = input()
        nova = ''
        for i in frase:
            if i == ' ':
                nova += i
            elif i in fileira_1:
                idx = fileira_1.index(i)
                nova += fileira_1[idx-1]
            elif i in fileira_2:
                idx = fileira_2.index(i)
                nova += fileira_2[idx-1]
            elif i in fileira_3:
                idx = fileira_3.index(i)
                nova += fileira_3[idx-1]
            elif i in fileira_4:
                idx = fileira_4.index(i)
                nova += fileira_4[idx-1]
        print(nova)
    except EOFError:
        break
    