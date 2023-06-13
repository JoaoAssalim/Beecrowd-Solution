n = int(input())
s = input().split("b")
c = 0

for i in s:
    if len(i) > 1:
        c += len(i)

print(c)