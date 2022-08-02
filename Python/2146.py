while True:
    try:
        senha = int(input())
        print(senha-1)
    
    except EOFError:
        break