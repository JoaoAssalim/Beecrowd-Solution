nums = []

while True:
    idd = int(input())
    
    if idd >= 0:
        nums.append(idd)
    else:
        break

print(f'{sum(nums)/len(nums):.2f}')