s = input().split()
if all(i == '1' or i == '0' for i in s):
    print("S")
else:
    print("F")