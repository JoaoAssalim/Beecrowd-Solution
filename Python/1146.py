while True:
    ent = int(input())
    if ent == 0:
        break
    else:
        for i in range(1, ent):
            print(i, end=" ")
        print(ent)