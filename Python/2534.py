while True:
    try:
        N, Q = list(map(int, input().split()))
        
        notas = []
        for i in range(N):
            notas.append(int(input()))
        
        notas = sorted(notas, reverse=True)
        
        for y in range(Q):
            pos = int(input())
            print(notas[pos-1])
    except EOFError:
        break
