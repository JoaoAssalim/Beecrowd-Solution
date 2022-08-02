km = 0

for i in range(int(input())):
    dist, vel = list(map(int, input().split()))
    km += dist * vel
print(km)