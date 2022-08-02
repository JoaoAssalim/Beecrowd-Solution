a, b = list(map(float, input().split()))
print(f'{((((1.0 + a/100.00) * (1.0 + b/100.00)) - 1.0) * 100.0):.6f}')
