top = [1,3,5,10,25,50,100]
k = int(input())
c = 0

while True:
    if top[c] >= k:
        print(f'Top {top[c]}')
        break
    c+=1