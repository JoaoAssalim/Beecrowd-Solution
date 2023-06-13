count = 0
for i in range(int(input())):
    a,b = list(map(int, input().split()))
    count += a/b

print("OK" if count <= 1 else "FAIL")
