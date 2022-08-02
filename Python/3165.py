n = int(input())
primos = []

for i in range(2, n+1):
    mult=0
    for count in range(2,i):
        if (i % count == 0):
            mult += 1
    if mult == 0:
        primos.append(i)

while True:
    if len(primos) > 2:
        if primos[-1] - primos[-2] <= 2:
            break
        else:
            primos.pop()
    else:
        break

print(f'{primos[-2]} {primos[-1]}')
