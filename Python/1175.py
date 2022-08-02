nums = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]

for i in range(0, len(nums)):
    y = int(input())
    nums[i] = y

index_comeco = 0
index_fim = 19

while index_fim > 9:
    nums[index_comeco], nums[index_fim] = nums[index_fim], nums[index_comeco]
    index_comeco += 1
    index_fim -= 1

count = 0

for x in nums:
    print(f'N[{count}] = {int(x)}')
    count += 1