peso = 0
preco = 0
N = int(input())
for i in range(N):
    p = float(input())
    frutas = input().split()
    print(f'day {i+1}: {len(frutas)} kg')
    preco += p
    peso += len(frutas)

print(f'{peso/N:.2f} kg by day')
print(f'R$ {preco/N:.2f} by day')
