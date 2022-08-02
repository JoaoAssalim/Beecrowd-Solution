num_pos = 0
for i in range(6):
    num = float(input())
    if num > 0:
        num_pos += 1
print(f'{num_pos} valores positivos')