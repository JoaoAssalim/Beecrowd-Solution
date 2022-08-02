num_pos = 0
for i in range(5):
    num = int(input())
    if num % 2 == 0:
        num_pos += 1

print(f'{num_pos} valores pares')