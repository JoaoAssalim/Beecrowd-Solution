num_pos = 0
pos = []
media = 0
for i in range(6):
    num = float(input())
    if num > 0:
        num_pos += 1
        pos.append(num)

for num in pos:
    media += num
print(f'{num_pos} valores positivos')
print(f'{media/num_pos:.1f}')