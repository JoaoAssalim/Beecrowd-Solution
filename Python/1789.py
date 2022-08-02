while True:
    try:
        quant = int(input())
        velocidades = input().split()
        velocidades = [int(x) for x in velocidades]
        maxima = max(velocidades)
        
        if int(maxima) < 10:
            print(1)
        elif int(maxima) >= 10 and int(maxima) < 20:
            print(2)
        elif int(maxima) >= 20:
            print(3)
        
    except EOFError:
        break