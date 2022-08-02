s = input()
one = 0

for i in s:
    if i == '1':
        one += 1
if one %2==0:
    s += '0'
else:
    s += '1'
print(s)