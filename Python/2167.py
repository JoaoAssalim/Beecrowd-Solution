idc = 0
num = 0
rang = int(input())
n = input().split()
for cnt, i in enumerate(n):
    if cnt == 0:
        num = int(i)
    if idc == 0 and int(i) < num:
        idc = cnt + 1
        num = 0
    elif int(i) > num:
        num = int(i)
print(idc)
