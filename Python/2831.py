n = int(input())
l = list(map(int, input().split()))
ult = 0

ver = True
for i in l:
    if i - ult > 8:
        ver = False
        break
    ult = i

print("S" if ver else "N")