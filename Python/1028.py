def mdc(a,b):
    while b !=0:
        resto = a % b
        a = b
        b = resto

    return a

for i in range(int(input())):
    a, b = list(map(int,input().split()))
    print(mdc(a,b))
