num = list(map(int, input().split()))
A = num[0]
N = num[-1]
total = 0

for i in range(N):
    total += A + i
    
print(total)
