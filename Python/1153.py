fat = int(input())
num = 1

while fat > 1:
    num *= fat
    fat -= 1
print(num)