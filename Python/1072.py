n = int(input())
nums = []
in_n = 0
out = 0

for i in range(n):
    x = int(input())
    nums.append(x)

for num in nums:
    if num >= 10  and num <= 20:
        in_n += 1
    else:
        out += 1

print(f'{in_n} in')
print(f'{out} out')