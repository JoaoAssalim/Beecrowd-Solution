while True:
    try:
        n = int(input())
        sec = n // 100
        
        if n % 100 != 0: sec += 1
        print(sec)
        
    except EOFError:
        break
