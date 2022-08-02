s = 0
divs = 1
base = 1

for i in range(1, 20):
    s += base/divs
    base += 2
    divs *= 2
print(f'{s:.2f}')