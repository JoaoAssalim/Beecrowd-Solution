m = int(input())
a = int(input())
b = int(input())

if m >= 40 and m <=110 and a >= 1 and a < m and b >= 1 and b < m and a!=b:
    idade = m - a - b
    if idade > a and idade > b:
        print(idade)
    elif a > idade and a > b:
        print(a)
    else:
        print(b)