from math import factorial

while True:
    num = input()
    soma = 0
    
    if num == '0':
        break
    else:
        leng = len(num)
        for i in num:
            soma += int(i)*factorial(leng)
            leng -= 1
        print(soma)