while True:
    try:
        A,B = list(map(int, input().split()))
        A = A*2
        print(A*B)
    except EOFError:
        break