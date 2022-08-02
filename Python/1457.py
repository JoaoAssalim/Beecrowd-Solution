for i in range(int(input())):
    fatorial = input()
    num2 = fatorial.count('!')
    num1 = int(fatorial[:len(fatorial)-num2])
    total = 1
    
    while True:
        if num1 <= 0:
            break
        total *= num1
        num1 = num1-num2
        
    print(total)
