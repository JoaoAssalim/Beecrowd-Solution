import math

a,b = list(map(int, input().split()))

q = (a - (a % abs(b))) // b
r = a % abs(b)

print(q, r)
