ver = False
while True:
    try:
        n = int(input())
        if ver:
            print()
        b = False
        an = False
        
        if n % 400 == 0 or (n % 4 == 0 and n % 100 != 0):
            if n % 55 == 0:
                b = True
            print('This is leap year.')
            an = True
        if n % 15 == 0:
            print("This is huluculu festival year.")
            an = True
        if b:
            print('This is bulukulu festival year.')
            an = True
        
        if an == False:
            print("This is an ordinary year.")
        
        ver = True
    except EOFError:
        break
