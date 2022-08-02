for i in range(int(input())):
    a,b = map(int, input().split())
    nova = ''
    for x in range(a, b+1):
        nova += str(x)
    nova += nova[::-1]
    print(nova)