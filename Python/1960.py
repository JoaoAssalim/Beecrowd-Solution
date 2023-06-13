# I é 1, V é 5, X é 10, L é 50, C é 100, D é 500 e M é 1000.
n = input()
s = ''

aux = 0
ver = 0
for i in n[::-1]:
    saux = ''
    if aux == 0:
        if int(i) <= 3:
            saux += 'I'*int(i)
        elif int(i) == 4:
            saux += "IV"
        elif int(i) == 5:
            saux += 'V'
        elif int(i) <= 8:
            saux += "V" + "I"*(int(i)-5)
        elif int(i) == 9:
            saux += "IX"
    elif aux == 1:
        if int(i) <= 3:
            saux += "X" * int(i)
        elif int(i) == 4:
            saux += "XL"
        elif int(i) == 5:
            saux += 'L'
        elif int(i) <= 8:
            saux += "L" + "X"*(int(i)-5)
        elif int(i) == 9:
            saux += "XC"
    elif aux == 2:
        if int(i) <= 3:
            saux += "C" * int(i)
        elif int(i) == 4:
            saux += "CD"
        elif int(i) == 5:
            saux += 'D'
        elif int(i) <= 8:
            saux += "D" + "C"*(int(i)-5)
        elif int(i) == 9:
            saux += "CM"
    else:
        if int(i) == 1:
            saux += 'M'
    s += saux[::-1]
    
    aux += 1

print(s[::-1])