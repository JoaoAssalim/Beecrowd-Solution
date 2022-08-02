while True:
    try:
        a = input()
        b = input()
                
        if b in a:
            print("Resistente")
        else:
            print("Nao resistente")
    except EOFError:
        break
