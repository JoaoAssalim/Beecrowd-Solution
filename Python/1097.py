i = 1
j = 7
for x in range(5):
    b = j
    for x in range(3):
        print(f'I={i} J={b}')
        b -= 1
    i += 2
    j += 2