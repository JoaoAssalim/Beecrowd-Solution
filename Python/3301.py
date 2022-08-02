n = input().split()
for c, i in enumerate(n):
    n[c] = int(i)

a = int(n[0])
b = int(n[1])
c = int(n[2])


if max(n) == a and min(n) == b:
    print('luisinho')
elif max(n) == a and min(n) == c:
    print('zezinho')
    
elif max(n) == b and min(n) == a:
    print('luisinho')
elif max(n) == b and min(n) == c:
    print('huguinho')

elif max(n) == c and min(n) == a:
    print('zezinho')
elif max(n) == c and min(n) == b:
    print('huguinho')
