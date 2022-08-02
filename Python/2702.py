a, b, c = list(map(int, input().split()))
a1, b1, c1 = list(map(int, input().split()))

A = a - a1
B = b - b1
C = c - c1

total = 0
if A < 0: 
    A *= -1
    total += A
if B < 0:
    B *= -1
    total += B
if C < 0:
    C *= -1
    total += C

print(total)
