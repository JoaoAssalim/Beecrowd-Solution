x = int(input())
y = int(input())
soma = 0
if y < x:
    x,y=y,x
    
for i in range(x, y):
    if not i %13 == 0:
        soma += i
print(soma)