for i in range(int(input())):
    n = int(input())
    lista = input().split()
    dist = set()
    
    for x in lista:
        dist.add(int(x))
    print(len(dist))
