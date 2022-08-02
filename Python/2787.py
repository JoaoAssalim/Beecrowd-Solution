A = int(input())
B = int(input())

if A % 2 == 0 and B % 2 == 0:
    print(1)
elif A % 2 == 0 and B % 2:
    print(0)
elif A % 2 and B % 2 == 0:
    print(0)
else:
    print(1)
